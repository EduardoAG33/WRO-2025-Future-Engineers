import sensor, image, utime, micropython
import LPF2
micropython.alloc_emergency_exception_buf(200)

SHOW_DEBUG = True   

modes = [LPF2.mode('OV-ALL', size=8, type=LPF2.DATA16, format='3.0')]

# Umbrales (LAB) — ajusta en pista
TH_RED   = (18, 60, 19, 127, 6, 127)
TH_GREEN = (0, 28, -128, -13, 8, 127)
TH_BLACK = (0, 30, -10, 10, -10, 10)

# ROIs (x, y, w, h)
ROI1 = (0,   50, 80,  25)   # izquierda (negro)
ROI2 = (80,  50, 80,  25)   # derecha  (negro)
ROI3 = (20,  20, 120, 50)   # pilares (rojo/verde)

PIXELS_T = 40
AREA_T   = 40
MERGE    = True

# LPF2 / EV3 (todo posicional)
lpf2 = LPF2.EV3_LPF2(3, 'P4', 'P5', modes, 85, 4, 5)
lpf2.initialize()

# Cámara
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)  # 160x120
sensor.skip_frames(time=1500)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)

def best_blob(blobs):
    return None if not blobs else max(blobs, key=lambda b: b.area())

def clamp_i16(v):
    return -32768 if v < -32768 else 32767 if v > 32767 else int(v)

def max_area_in_roi(img, th, roi):
    bs = img.find_blobs([th], roi=roi,
                        pixels_threshold=PIXELS_T, area_threshold=AREA_T,
                        merge=MERGE)
    if SHOW_DEBUG and bs:
        # muestra contornos de negro (pared) tenues
        for bb in bs:
            img.draw_rectangle(bb.rect(), color=(80,80,80))
    b = best_blob(bs)
    return 0 if b is None else b.area()

def map_xy(val, max_val):
    if val == 0:  # “no blob”
        return 0
    return int(((val - (max_val/2)) / (max_val/2)) * 100)

while True:
    if not lpf2.connected:
        try:
            lpf2.sendTimer.deinit()
        except Exception:
            pass
        utime.sleep_ms(50)
        lpf2.initialize()
        continue

    img = sensor.snapshot()

    # ---- DIBUJO DE ROIs / GUI ----
    if SHOW_DEBUG:
        # ROIs
        img.draw_rectangle(ROI1, color=(0,180,255), thickness=1)   # cian: izquierda
        img.draw_string(ROI1[0]+2, max(0, ROI1[1]-10), "ROI1-L", color=(0,180,255))
        img.draw_rectangle(ROI2, color=(255,180,0), thickness=1)   # naranja: derecha
        img.draw_string(ROI2[0]+2, max(0, ROI2[1]-10), "ROI2-R", color=(255,180,0))
        img.draw_rectangle(ROI3, color=(0,255,0), thickness=1)     # verde: pilares
        img.draw_string(ROI3[0]+2, max(0, ROI3[1]-10), "ROI3-P", color=(0,255,0))
        # líneas de centro (para ver el 0 de la escala -100..100)
        img.draw_line(80, 0, 80, 120, color=(200,200,200))
        img.draw_line(0, 60, 160, 60, color=(200,200,200))

    # ---- PILARES (ROI3) ----
    g = best_blob(img.find_blobs([TH_GREEN], roi=ROI3,
                                 pixels_threshold=PIXELS_T, area_threshold=AREA_T, merge=MERGE))
    r = best_blob(img.find_blobs([TH_RED], roi=ROI3,
                                 pixels_threshold=PIXELS_T, area_threshold=AREA_T, merge=MERGE))

    if SHOW_DEBUG and g:
        img.draw_rectangle(g.rect(), color=(0,255,0), thickness=1)
        img.draw_cross(g.cx(), g.cy(), color=(0,255,0), size=6, thickness=2)
        img.draw_string(g.cx()+3, max(0, g.cy()-10), "G", color=(0,255,0))
    if SHOW_DEBUG and r:
        img.draw_rectangle(r.rect(), color=(255,0,0), thickness=1)
        img.draw_cross(r.cx(), r.cy(), color=(255,0,0), size=6, thickness=2)
        img.draw_string(r.cx()+3, max(0, r.cy()-10), "R", color=(255,0,0))

    # Normaliza XY a -100..100 (QQVGA: 160x120)
    g_x = 0 if g is None else map_xy(g.cx(), 160)
    g_y = 0 if g is None else map_xy(g.cy(), 120)
    r_x = 0 if r is None else map_xy(r.cx(), 160)
    r_y = 0 if r is None else map_xy(r.cy(), 120)

    # Paredes (negro) izquierda/derecha
    left_area  = max_area_in_roi(img, TH_BLACK, ROI1)
    right_area = max_area_in_roi(img, TH_BLACK, ROI2)

    if SHOW_DEBUG:
        img.draw_string(2, 2,  "Gx:{:>4} Gy:{:>4}".format(g_x, g_y), color=(255,255,255))
        img.draw_string(2, 14, "Rx:{:>4} Ry:{:>4}".format(r_x, r_y), color=(255,255,255))
        img.draw_string(2, 26, "L:{:>5} R:{:>5}".format(left_area, right_area), color=(255,255,0))

    # ---- Envío a EV3 (8 x int16) ----
    DataToSend = [
        clamp_i16(g_x),        
        clamp_i16(g_y),        
        clamp_i16(r_x),        
        clamp_i16(r_y),        
        clamp_i16(left_area),  
        clamp_i16(right_area), 
    ]

    try:
        if lpf2.current_mode == 0:
            lpf2.load_payload('Int16', DataToSend)
    except Exception:
        try:
            lpf2.sendTimer.deinit()
        except Exception:
            pass
        utime.sleep_ms(20)
        lpf2.initialize
