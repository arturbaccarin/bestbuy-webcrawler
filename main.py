import db
import crawler as cr

if __name__ == '__main__':
    db.create_table()

    url_homepage = 'https://www.bestbuy.com/'
    driver = cr.execute_web_driver()
    categories_urls = cr.get_home_page_categories(url_homepage, driver)
    products_urls = cr.get_products_urls_in_categories(categories_urls[:2], driver)
    cr.save_products_info(products_urls, driver)


    products_urls = [
         'https://www.bestbuy.com/site/epson-pro-cinema-4050-4k-via-upscaling-3lcd-projector-with-high-dynamic-range-black/6314556.p?skuId=6314556', 
 'https://www.bestbuy.com/site/insignia-114-outdoor-projector-screen-white/6318225.p?skuId=6318225',
 'https://www.bestbuy.com/site/hisense-px1-pro-triple-laser-ultra-short-throw-home-theater-projector-4k-uhd-hdr-android-tv-dolby-atmos-2200-lumens-gray/6502770.p?skuId=6502770',
 'https://www.bestbuy.com/site/lg-cinebeam-hu70lab-4k-wireless-smart-dlp-projector-with-high-dynamic-range-black/6416036.p?skuId=6416036',   
 'https://www.bestbuy.com/site/lg-cinebeam-hu915qb-premium-4k-uhd-laser-ust-projector-black/6516244.p?skuId=6516244',
 'https://www.bestbuy.com/site/optoma-uhz45-4k-uhd-laser-home-theater-and-gaming-projector--3800-lumens-for-lights-on-viewing--240hz-refresh-rate-white/6510152.p?skuId=6510152',
 'https://www.bestbuy.com/site/lg-cinebeam-full-hd-smart-dlp-portable-projector-with-hdr10-white/6486495.p?skuId=6486495',
 'https://www.bestbuy.com/site/epson-epiqvision-ultra-ls500-4k-via-upscaling-pro-uhd-short-throw-laser-projector-4000-lumens-hdr-android-tv-sports-white/6429447.p?skuId=6429447',
 'https://www.bestbuy.com/site/epson-home-cinema-2200-1080p-3lcd-projector-with-android-tv-white/6479785.p?skuId=6479785',
 'https://www.bestbuy.com/site/lg-cinebeam-hu710pw-4k-uhd-hybrid-home-cinema-projector-white/6496325.p?skuId=6496325',
 'https://www.bestbuy.com/site/yaber-buffalo-u2-native-720p-entertainment-lcd-projector-with-projector-screen-white/6508277.p?skuId=6508277',
 'https://www.bestbuy.com/site/optoma-uhd35-true-4k-uhd-next-generation-gaming-projector-with-3600-lumens-4-2ms-response-time-with-enhanced-gaming-mode-white/6450785.p?skuId=6450785',
 'https://www.bestbuy.com/site/yaber-buffalo-pro-u9-native-1080p-entertainment-lcd-projector-with-projector-screen-black/6508883.p?skuId=6508883',
 'https://www.bestbuy.com/site/epson-ex5280-3lcd-xga-projector-with-built-in-speaker-white/6457640.p?skuId=6457640',
 'https://www.bestbuy.com/site/cinebeam-dual-laser-streaming-4k-uhd-smart-portable-projector-with-lg-webos-and-hdr10-white/6494728.p?skuId=6494728',
 'https://www.bestbuy.com/site/lg-cinebeam-hu715q-4k-uhd-laser-ust-projector-white/6496327.p?skuId=6496327',
 'https://www.bestbuy.com/site/nebula-by-anker-cosmos-laser-4k-portable-projector-black-gray/6510120.p?skuId=6510120',
 'https://www.bestbuy.com/site/lg-cinebeam-hu915qe-premium-4k-uhd-laser-ust-projector-white/6516258.p?skuId=6516258',
 'https://www.bestbuy.com/site/lg-ph510p-hd-led-3d-portable-cinebeam-projector-white/6446229.p?skuId=6446229']