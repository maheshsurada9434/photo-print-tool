# Temporary check (not part of the app): runs the on-device AI features against a real face photo.
import subprocess, time, os
pg = None
from playwright.sync_api import sync_playwright
os.makedirs('shots', exist_ok=True)
srv = subprocess.Popen(['python3', '-m', 'http.server', '8800'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
log = []
try:
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1300, 'height': 1000})
        pg.on('pageerror', lambda e: log.append('PAGEERROR ' + str(e)))
        pg.on('console', lambda m: m.type == 'error' and log.append('CONSOLE ' + m.text))
        pg.goto('http://localhost:8800/index.html'); pg.wait_for_timeout(1500)
        pg.set_input_files('#file', ['face.jpg']); pg.wait_for_timeout(1500); log.append('items=' + str(pg.locator('.item').count()) + ' toast=' + pg.locator('#toast').inner_text()); pg.screenshot(path='shots/0-loaded.png')
        pg.locator('.item').first.get_by_role('button', name='Background colour').click()
        pg.locator('.item').first.get_by_role('button', name='White').click()
        t0 = time.time()
        pg.wait_for_timeout(1500)
        pg.wait_for_function("!document.querySelector('.item .status') || document.querySelector('.item .status').textContent === ''", timeout=120000)
        log.append(f'cutout done in {time.time()-t0:.1f}s, plain-wall pressed = ' + str(pg.locator('.item').first.get_by_role('button', name='Plain wall').get_attribute('aria-pressed')))
        pg.wait_for_timeout(800); pg.screenshot(path='shots/1-cutout.png')
        pg.locator('.item').first.get_by_role('button', name='Done').click()
        pg.click('#fitAll'); pg.wait_for_timeout(5000); log.append('fitAll toast: ' + pg.locator('#toast').inner_text())
        pg.wait_for_timeout(800); pg.screenshot(path='shots/2-fitted.png')
        pg.locator('.item').first.locator('.thumb').click(); pg.wait_for_timeout(600); pg.screenshot(path='shots/3-dialog.png')
        b.close()
except Exception as e:
    import traceback; log.append('EXCEPTION ' + traceback.format_exc()[-1500:])
    try: pg.screenshot(path='shots/error.png')
    except Exception: pass
finally:
    srv.kill()
    open('shots/log.txt', 'w').write('\n'.join(log)); print('\n'.join(log))
