"""買三送一大禮包落地頁 v1：照片、去背圖、手帳週計畫手寫片段 → img/、gif/clips/p_week（2026-11-25）"""
import os, shutil, subprocess
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
B = "/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/04_內容企劃/_多產品/落地頁改版設計_1122/"
XN = B + '11.24_煦暖曆_落地頁改版_v9_六色經典底座同步輪播_規格圖裁上方/_原始檔/img/'
PL = B + '11.24_手帳_落地頁改版_v9_覺察卡改不怕不知道怎麼寫/'
QT = B + '11.25_語錄卡_落地頁改版_v5_照幹話曆結構_圓角卡片收藏盒/_原始檔/img/'
PH = B + '11.25_手機版日曆_落地頁改版_v8_說明句一行_大標改遠距離好友/_原始檔/img/'
CUT = B + '11.24_全站_方案卡首圖_v1/工作檔/'
CUT2 = B + '11.24_旅行機票日曆_方案卡首圖_v2/工作檔/去背/'
CUT3 = "/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/01_廣告投放/_多產品/圖文/組合優惠貼紙版_1124/工作檔/去背/"
I = D + '/img/'; os.makedirs(I, exist_ok=True)

def crop45(src, dst, cx=0.5, cy=0.5, w=900):
    im = Image.open(src).convert('RGB'); W, H = im.size
    if W / H > 0.8: h = H; ww = int(H * 0.8)
    else: ww = W; h = int(W * 1.25)
    x0 = int(min(max(cx * W - ww / 2, 0), W - ww)); y0 = int(min(max(cy * H - h / 2, 0), H - h))
    im.crop((x0, y0, x0 + ww, y0 + h)).resize((w, int(w * 1.25)), Image.LANCZOS).save(dst, quality=90)

# 片頭四格（產品在生活裡）
crop45(XN + 'q1.jpg', I + 'o1.jpg')
crop45(PH + 'p1.jpg', I + 'o2.jpg')
crop45(PL + '_原始檔/img/q1.jpg', I + 'o3.jpg', cx=0.45)
crop45(QT + 'p1.jpg', I + 'o4.jpg')
# 片尾彩蛋、收尾
shutil.copy(XN + 'q4.jpg', I + 'gift.jpg')
shutil.copy(XN + 'end.jpg', I + 'end.jpg')
shutil.copy(QT + 's10.jpg', I + 'qt5.jpg')
# 去背
cp = {'h_cal': CUT + '去背/cut_煦暖曆經典靜灣.png', 'h_pl': CUT + '去背/cut_開窗暖杏.png', 'h_qt': CUT + '去背/cut_qte1.png',
      'h_ph': CUT + 'assets/phone_0101.png',
      'c_xn': CUT + '去背/cut_煦暖曆經典靜灣.png', 'c_gh': CUT + '去背/cut_幹話天藍.png', 'c_fl': CUT + '去背/cut_鮮花繡球晴藍.png',
      'c_tr': CUT2 + 'cut_夜航.png', 'c_fh': CUT + '去背/cut_法華松柏綠.png',
      'ph_xn': CUT + 'assets/phone_0101.png', 'ph_gh': CUT + 'assets/phone_gh_0102.png', 'ph_tr': CUT + 'assets/phone_tr_1225.png',
      'pl_a': CUT3 + 'cut_開窗暖杏.png', 'pl_b': CUT3 + 'cut_開窗霧藍.png', 'pl_c': CUT3 + 'cut_開窗墨綠.png', 'pl_d': CUT3 + 'cut_開窗米白.png'}
for k, f in cp.items():
    im = Image.open(f).convert('RGBA'); bb = im.getbbox(); im = im.crop(bb)
    im.thumbnail((900, 900), Image.LANCZOS); im.save(I + k + '.png')
# 手帳週計畫手寫（手帳落地頁 v9 05a 的 MP4，只裁內頁那塊，4:5）
od = D + '/gif/clips/p_week'; shutil.rmtree(od, ignore_errors=True); os.makedirs(od)
subprocess.run(['ffmpeg', '-v', 'error', '-i', PL + '動圖_MP4備用/05a_週計畫.mp4', '-vf',
                'setpts=PTS/1.25,fps=15,crop=980:1225:50:536,scale=1080:1350:flags=lanczos', '-q:v', '2', od + '/%03d.jpg'], check=True)
print('p_week', len(os.listdir(od)))
print(sorted(os.listdir(I)))
