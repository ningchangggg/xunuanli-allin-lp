"""買三送一大禮包落地頁 v1 實拍片段（2026-11-25）。
- x_tear：煦暖曆 麻豆 C0246 撕下今天（同煦暖曆落地頁 v9）
- p_write／p_flat：手帳 麻豆 C0285 翻開寫字、丁丁 C0148 俯拍平攤（同手帳落地頁 v9）
- q_draw：語錄卡 麻豆 C0191 打開收藏盒抽一張（同語錄卡落地頁 v5）
- c_where／c_unlock：手機版煦暖曆落地頁 v5 的 Widget 情境片段（直接複製畫格）
裁 4:5、1080×1350、15fps。"""
import subprocess,os,shutil,sys
from concurrent.futures import ThreadPoolExecutor
R="/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/01_廣告投放/"
FPS=15
C={ # name: (src, t0, t1, speed, cy, rotate, sat)
 'x_tear': (R+'煦暖曆/毛片/麻豆_影片_0812/C0246.mp4', 2.6, 7.4, 1.2, 0.30, '', 1.3),
 'p_write':(R+'手帳/毛片/麻豆_影片_0812/C0285.mp4', 12.8, 19.0, 1.4, 0.5, '', 1.3),
 'p_flat': (R+'手帳/毛片/丁丁_新拍_1110_調色對齊麻豆/C0148.mp4', 16.5, 23.5, 1.3, 0.5, 'transpose=2', 1.45),
 'q_draw': (R+'語錄卡/毛片/麻豆_影片_0812/C0191.mp4', 0.8, 5.2, 1.1, 0.30, '', 1.12),
}
def run(item):
    n,(src,t0,t1,sp,cy,rot,sat)=item
    od=os.path.dirname(os.path.abspath(__file__))+f'/clips/{n}'; shutil.rmtree(od,ignore_errors=True); os.makedirs(od)
    vf=(f"scale=in_color_matrix=bt709:out_color_matrix=bt709,{rot+',' if rot else ''}setpts=PTS/{sp},fps={FPS},"
        f"crop=iw:iw*1.25:0:(ih-iw*1.25)*{cy},scale=1080:1350:flags=lanczos,eq=saturation={sat}:contrast=1.04")
    subprocess.run(['ffmpeg','-v','error','-ss',str(t0),'-t',str(t1-t0),'-i',src,'-vf',vf,'-q:v','2',f'{od}/%03d.jpg'],check=True,stdin=subprocess.DEVNULL)
    return n,len(os.listdir(od))
sel=sys.argv[1:] or list(C)
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(run,[(k,C[k]) for k in sel]): print(r)
