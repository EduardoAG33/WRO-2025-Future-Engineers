# --- OpenMV: Pilares (ID/X/Collision/AREA) + Piso(error BLANCO/AZUL/NARANJA) + Magenta(X) ---
# LPF2 Payload (Int16, size=8): [ ID, X, Collision, error, area_px, MAG_X, 0, 0 ]

# TH_COLOR = (Lmin, Lmax, Amin, Amax, Bmin, Bmax)  -> siempre de menor a mayor

import sensor, image, time, utime, micropython
import LPF2
micropython.alloc_emergency_exception_buf(200)

# ===== Switches / Debug =====
SHOW_DEBUG        = True
DRAW_BOXES        = True
DRAW_TEXT         = True
X_AS_NORMALIZED   = True
USE_MULTI_RANGES  = True

# ===== LPF2 (8 Int16 para EV3 con 8 salidas) =====
modes = [LPF2.mode('OV-ALL', size=8, type=LPF2.DATA16, format='3.0')]
lpf2 = LPF2.EV3_LPF2(3, 'P4', 'P5', modes, 85, 4, 5)
lpf2.initialize()

# ===== Umbrales (LAB) — solo 1 y 2 por color =====
# Pilares
TH_RED_1   = (0, 58, 15, 53, -128, 19)
TH_RED_2   = (0, 42, 33, 70,  14, 62)
TH_GREEN_1 = (0, 74, -128, -22, 9, 127)
TH_GREEN_2 = (0,100,  -29,  -50, 22,  65)
# Piso: BLANCO + AZUL + NARANJA
TH_WHITE_1  = (54, 100, -20,   3,   -8,  16)
TH_WHITE_2  = (35, 100, -35,  15,  -35,  25)
TH_BLUE_1   = (0,   55,  -7,  57, -128,  -3)
TH_BLUE_2   = (0,   40, -10, 127, -128,  -5)
TH_ORANGE_1 = (57, 100,   4, 127,   7,  68)
TH_ORANGE_2 = (0,  100,  16,  72,  20,  71)
# Magenta (X global)
TH_MAGENTA_1 = (0, 100,  8, 80, -128,  -7)
TH_MAGENTA_2 = (0,  80, 15, 75,  -25,  45)

# Activación (1 y 2)
USE_RED_1,   USE_RED_2     = True,  False
USE_GREEN_1, USE_GREEN_2   = True,  False
USE_WHITE_1A, USE_WHITE_2A = True,  False
USE_BLUE_1A,  USE_BLUE_2A  = True,  False
USE_ORNG_1A,  USE_ORNG_2A  = True,  False
USE_MAG_1,    USE_MAG_2    = True,  True

def _active_by_flags(th_list, flags):
    act = [t for t, f in zip(th_list, flags) if f and t is not None]
    if not act: act = [th_list[0]]
    return act if USE_MULTI_RANGES else [act[0]]

THS_RED        = _active_by_flags([TH_RED_1,   TH_RED_2],   [USE_RED_1,   USE_RED_2])
THS_GREEN      = _active_by_flags([TH_GREEN_1, TH_GREEN_2], [USE_GREEN_1, USE_GREEN_2])
TH_WHITE_SET   = _active_by_flags([TH_WHITE_1,  TH_WHITE_2],  [USE_WHITE_1A, USE_WHITE_2A])
TH_BLUE_SET    = _active_by_flags([TH_BLUE_1,   TH_BLUE_2],   [USE_BLUE_1A,  USE_BLUE_2A])
TH_ORANGE_SET  = _active_by_flags([TH_ORANGE_1, TH_ORANGE_2], [USE_ORNG_1A,  USE_ORNG_2A])
TH_MAG_SET     = _active_by_flags([TH_MAGENTA_1, TH_MAGENTA_2], [USE_MAG_1, USE_MAG_2])

# Piso = blanco + azul + naranja
TRACK_THS = TH_WHITE_SET + TH_BLUE_SET + TH_ORANGE_SET

# ===== Filtros / forma (pilares) =====
AREA_TH_RG_PX     = 30
MIN_H_PILLAR      = 12
MIN_H_OVER_W      = 1.20
MAX_TILT_DEG      = 35
MIN_PILLAR_AREA   = 60
MAX_LINE_H        = 12
MAX_LINE_W_OVER_H = 2.0

# ===== Blobs / gating =====
PIX_TH  = 8
AREA_TH = 8
MERGE   = True
MARGIN  = 5

# ===== Cámara =====
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)   # 320x240
sensor.set_auto_gain(True); sensor.set_auto_whitebal(True); sensor.set_auto_exposure(True)
sensor.skip_frames(time=800)
sensor.set_auto_gain(False); sensor.set_auto_whitebal(False)
sensor.set_auto_exposure(False, exposure_us=25000)
sensor.skip_frames(time=300)

# ===== Geometría =====
IMG_W, IMG_H = 320, 240
CENTER_X     = IMG_W // 2

# Pilares
ROI_MID  = (0, 80, 320, 40)
ROI_LOW  = (60, 120, 200, 60)
PILLARS_ROI = (0, min(ROI_MID[1], ROI_LOW[1]), IMG_W,
               (max(ROI_MID[1]+ROI_MID[3], ROI_LOW[1]+ROI_LOW[3]) - min(ROI_MID[1], ROI_LOW[1])))
COLLISION_ROI      = (120, 135, 80, 10)
COLLISION_AREA_MIN = 40

# Piso
ROI_H   = 10
ROI1    = (0,   130,  90, ROI_H)
ROI2    = (230, 130,  90, ROI_H)
BAND_Y  = ROI1[1]
BAND    = (0, BAND_Y, IMG_W, ROI_H)
COL_BAND = (90, 90, 90)

# ===== Filtros de señal =====
EMA_ALPHA = 1
ERR_ALPHA = 1
ema_left  = None
ema_right = None
err_ema   = None

# ===== Helpers =====
def clamp_i16(v): return -32768 if v < -32768 else 32767 if v > 32767 else int(v)
def clamp(v, lo, hi): return lo if v < lo else hi if v > hi else v
def best_blob_area(blobs): return None if not blobs else max(blobs, key=lambda b: b.area())
def looks_like_line(b): return (b.h() <= MAX_LINE_H) or ((b.w() / max(1, b.h())) >= MAX_LINE_W_OVER_H)
def is_vertical_pillar(b):
    if not b or b.area() < MIN_PILLAR_AREA or b.h() < MIN_H_PILLAR: return False
    if (b.h() / max(1, b.w())) < MIN_H_OVER_W: return False
    try:
        rot_deg = abs((b.rotation() or 0) * 57.29578) % 180.0
        tilt = min(abs(rot_deg - 90.0), abs((rot_deg + 90.0) - 90.0))
        if tilt > MAX_TILT_DEG: return False
    except: pass
    return True
def point_in_roi(x, y, roi): rx, ry, rw, rh = roi; return (rx <= x < rx+rw) and (ry <= y < ry+rh)
def corner_ll(b): x, y, w, h = b.rect(); return x, y + h - 1
def corner_lr(b): x, y, w, h = b.rect(); return x + w - 1, y + h - 1
def norm_x100(x_px): return clamp(int(((x_px - CENTER_X) / float(CENTER_X)) * 100.0), -100, 100)

def pct_from_blobs_touching_multi(img, roi, th_list):
    if roi is None or not th_list: return 0
    x, y, w, h = roi; roi_area = max(1, w*h)
    bs = img.find_blobs(th_list, roi=roi, pixels_threshold=PIX_TH, area_threshold=AREA_TH, merge=MERGE)
    if not bs: return 0
    px = sum(b.pixels() for b in bs if (b.y()+b.h()) >= (y + h - 2))
    return min(100, int((100.0 * px) / roi_area))
def pct_floor_touching(img, roi):
    pW = pct_from_blobs_touching_multi(img, roi, TH_WHITE_SET)
    pB = pct_from_blobs_touching_multi(img, roi, TH_BLUE_SET)
    pO = pct_from_blobs_touching_multi(img, roi, TH_ORANGE_SET)
    total = pW + pB + pO
    return 100 if total > 100 else total

def magenta_best_center_x(img):
    bs = img.find_blobs(TH_MAG_SET, pixels_threshold=PIX_TH, area_threshold=AREA_TH, merge=True)
    if not bs: return -1, None
    bb = best_blob_area(bs); nx = int(((bb.cx() - CENTER_X) * 100) / max(1, CENTER_X))
    return clamp(nx, -100, 100), bb

def find_rg_unified(img):
    r_bs = img.find_blobs(THS_RED, roi=PILLARS_ROI, pixels_threshold=PIX_TH, area_threshold=AREA_TH, merge=MERGE) or []
    g_bs = img.find_blobs(THS_GREEN, roi=PILLARS_ROI, pixels_threshold=PIX_TH, area_threshold=AREA_TH, merge=MERGE) or []
    r_bs = [b for b in r_bs if is_vertical_pillar(b) and not looks_like_line(b)]
    g_bs = [b for b in g_bs if is_vertical_pillar(b) and not looks_like_line(b)]
    return best_blob_area(r_bs), best_blob_area(g_bs)

# ===== Loop =====
clock = time.clock()
X_SENTINEL = -1

while True:
    if not lpf2.connected:
        try: lpf2.sendTimer.deinit()
        except: pass
        utime.sleep_ms(40)
        lpf2.initialize()
        continue

    clock.tick()
    img = sensor.snapshot()

    # --- Pilares ---
    rb, gb = find_rg_unified(img)
    sel_blob = None; ID = 0
    if gb and (not rb or gb.area() >= rb.area()): sel_blob, ID = gb, 3
    elif rb: sel_blob, ID = rb, 5

    X_CORNER = X_SENTINEL; area_px = 0
    if sel_blob:
        cx, cy = corner_ll(sel_blob) if ID == 3 else corner_lr(sel_blob)
        if point_in_roi(cx, cy, ROI_LOW) or point_in_roi(cx, cy, ROI_MID):
            X_CORNER = norm_x100(cx)
            area_px  = int(sel_blob.area())
            # saturación prudente para EV3
            if area_px < 0: area_px = 0
            if area_px > 30000: area_px = 30000
        else:
            ID, X_CORNER, area_px = 0, X_SENTINEL, 0

    # Colisión pilares
    col_g = img.find_blobs(THS_GREEN, roi=COLLISION_ROI, pixels_threshold=PIX_TH, area_threshold=AREA_TH)
    col_r = img.find_blobs(THS_RED,   roi=COLLISION_ROI, pixels_threshold=PIX_TH, area_threshold=AREA_TH)
    gb_c = best_blob_area(col_g); rb_c = best_blob_area(col_r)
    collision_id = 0
    if gb_c and (not rb_c or gb_c.area() >= rb_c.area()): collision_id = 3
    elif rb_c: collision_id = 5

    # --- Piso (BLANCO+AZUL+NARANJA) ---
    BAND = (0, BAND_Y, IMG_W, ROI_H)
    def floor_rect_in_band(img, band):
        bs = img.find_blobs(TRACK_THS, roi=band, pixels_threshold=PIX_TH, area_threshold=AREA_TH, merge=True)
        if not bs: return None
        x, y, w, h = best_blob_area(bs).rect()
        return (x, band[1], w, band[3])
    ROI_TF = floor_rect_in_band(img, BAND)
    if ROI_TF:
        L_int = (ROI1[0], ROI_TF[1], ROI1[2], ROI_TF[3])
        R_int = (ROI2[0], ROI_TF[1], ROI2[2], ROI_TF[3])
        L_pct, R_pct = pct_floor_touching(img, L_int), pct_floor_touching(img, R_int)
    else:
        L_pct, R_pct = 0, 0; L_int = R_int = None

    ema_left  = L_pct if ema_left is None else int((1-EMA_ALPHA)*ema_left  + EMA_ALPHA*L_pct)
    ema_right = R_pct if ema_right is None else int((1-EMA_ALPHA)*ema_right + EMA_ALPHA*R_pct)
    error_raw = ema_right - ema_left
    err_ema   = error_raw if err_ema is None else int((1-ERR_ALPHA)*err_ema + ERR_ALPHA*error_raw)

    # --- Magenta (X global) ---
    MAG_X, bb_mag = magenta_best_center_x(img)

    # --- Envío LPF2 (8 valores) ---
    DataToSend = [
        clamp_i16(ID),          # 1
        clamp_i16(X_CORNER),    # 2
        clamp_i16(collision_id),# 3
        clamp_i16(err_ema),     # 4
        clamp_i16(area_px),     # 5
        clamp_i16(MAG_X),       # 6
        0,                      # 7 padding
        0                       # 8 padding
    ]
    try:
        if lpf2.current_mode == 0:
            lpf2.load_payload('Int16', DataToSend)
    except Exception:
        try: lpf2.sendTimer.deinit()
        except: pass
        utime.sleep_ms(10); lpf2.initialize()

    # --- HUD: piso + info + dibujos (ROJO en orillas AL FINAL) ---
    if SHOW_DEBUG:
        # Piso (fondo + banda + ROI_TF)
        img.draw_rectangle(0, 0, 320, 70, color=(0,0,0), fill=True)
        img.draw_rectangle(BAND, color=COL_BAND)
        if ROI_TF: img.draw_rectangle(ROI_TF, color=(5,255,5))

        # Texto principal (incluye error y L/R%)
        img.draw_string(2, 2,  "L:%3d R:%3d Err:%4d" % (L_pct, R_pct, err_ema))
        img.draw_string(2, 12, "ID:%d  X:%4d  Col:%d  Area:%d  MAG_X:%d" %
                        (ID, X_CORNER, collision_id, area_px, MAG_X))

        # Pilares (ROIs y blobs)
        img.draw_rectangle(ROI_LOW, color=(255,255,0))
        img.draw_rectangle(ROI_MID, color=(255,200,0))
        img.draw_rectangle(PILLARS_ROI, color=(0,200,255))
        img.draw_rectangle(COLLISION_ROI, color=(0,255,255))
        if gb: img.draw_rectangle(gb.rect(), color=(0,255,0))
        if rb: img.draw_rectangle(rb.rect(), color=(255,0,0))
        if ID == 3 and gb:
            gx, gy = corner_ll(gb); img.draw_cross(gx, gy, color=(0,255,0))
        if ID == 5 and rb:
            rx, ry = corner_lr(rb); img.draw_cross(rx, ry, color=(255,0,0))

        # Magenta (solo dibujo del mejor blob)
        if bb_mag:
            img.draw_rectangle(bb_mag.rect(), color=(255, 0, 255))
            img.draw_cross(bb_mag.cx(), bb_mag.cy(), color=(255, 0, 255), size=8)

        # ORILLAS ROJAS AL FINAL (para que no se tapen)
        img.draw_rectangle(ROI1, color=(255,0,0))
        img.draw_rectangle(ROI2, color=(255,0,0))
        if ROI_TF and L_int: img.draw_rectangle(L_int, color=(90,90,90))
        if ROI_TF and R_int: img.draw_rectangle(R_int, color=(90,90,90))
