"""逐格截動圖區塊：場次（data-clip 換畫格）＋跑馬燈 s03（CSS 動畫 2.5 秒，25 格）。用法：python3 gif/render_gif.py [s05 s06 ...]"""
import asyncio, os, sys, shutil
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FR=D+'/gif/secframes'
async def main():
    sel=sys.argv[1:]
    async with async_playwright() as p:
        b=await p.chromium.launch(channel='chrome')
        pg=await b.new_page(viewport={'width':432,'height':900},device_scale_factor=2.5)
        await pg.goto('file://'+D+'/page.html'); await pg.wait_for_timeout(800); await pg.evaluate('document.fonts.ready')
        await pg.evaluate("document.getAnimations().forEach(a=>{a.pause();a.currentTime=0})")
        items=await pg.eval_on_selector_all('[data-clip]','els=>els.map(e=>[e.closest("section").id,e.dataset.clip])')
        for sec,clip in items:
            if sel and sec not in sel: continue
            od=f'{FR}/{sec}'; shutil.rmtree(od,ignore_errors=True); os.makedirs(od)
            fs=sorted(os.listdir(f'{D}/gif/clips/{clip}'))
            for i,f in enumerate(fs):
                u=f'gif/clips/{clip}/{f}'
                await pg.evaluate('''async ([c,u])=>{const im=new Image();im.src=u;await im.decode();document.querySelector(`[data-clip="${c}"]`).style.backgroundImage=`url(${u})`;await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))}''',[clip,u])
                await pg.locator('#'+sec).screenshot(path=f'{od}/{i+1:03d}.png')
            print(sec,clip,len(fs),flush=True)
        if not sel or 's03' in sel:
            od=f'{FR}/s03'; shutil.rmtree(od,ignore_errors=True); os.makedirs(od)
            for i in range(25):
                await pg.evaluate(f"document.getAnimations().forEach(a=>{{a.pause();a.currentTime={i*100}}})")
                await pg.locator('#s03').screenshot(path=f'{od}/{i+1:03d}.png')
            print('s03',25)
        await b.close()
asyncio.run(main())
