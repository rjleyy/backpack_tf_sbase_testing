from seleniumbase import BaseCase
from config.default import BASE_URL



class MainPage:

    def __init__(self, sb: BaseCase):

        # Locators
        self.sb = sb
        self.main_search_placeholder = "input[placeholder='Search']"
        self.main_search_input = '#navbar-search'
        self.main_search_price_buttons = 'div.buttons'
        self.main_page_logo = '.navbar-brand'
        self.main_game_navi = "img[src='/images/game_selector.png']"
        self.main_game_navi_tf2 = "img[alt='TF2']"
        self.main_game_navi_dota_2 = "img[src='/images/logo_570.svg']"
        self.main_game_navi_csgo = "a[href='/switch/730']"
        self.main_forum_page_link = 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)'
        self.main_pricing_dropdown = 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)'
        self.main_pricing_pricegrid_link = 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)'
        self.main_pricing_spreadsheet_link = "body div[role='navigation'] li li:nth-child(3) a:nth-child(1)"
        self.main_pricing_suggestions_link = "body div[role='navigation'] li li:nth-child(4) a:nth-child(1)"
        self.main_pricing_latest_changes_link = 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3) > ul:nth-child(2) > li:nth-child(5) > a:nth-child(1)'
        self.main_pricing_unusual_item_link = 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3) > ul:nth-child(2) > li:nth-child(8) > a:nth-child(1)'
        self.main_pricing_unusual_effect_link = 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3) > ul:nth-child(2) > li:nth-child(9) > a:nth-child(1)'
        self.main_pricing_marketplace_link = 'li:nth-child(12) a:nth-child(1)'
        self.main_trading_dropdown = "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)"
        self.main_trading_classified = 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)'
        self.main_trading_calc = 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > ul:nth-child(2) > li:nth-child(5) > a:nth-child(1)'
        self.main_trading_premium = "a[href='/premium/search']"
        self.main_statistics_dropdown = "li[id='nav_toplist'] a[class='dropdown-toggle']"
        self.main_statistics_browse_items = "a[href='/stats']"
        self.main_statistics_top_inv = "a[href='/top/backpacks']"
        self.main_statistics_top_dono = "a[href='/top/donators']"
        self.main_statistics_top_gift = "a[href='/top/generous']"
        self.main_statistics_most_accurate = '/html[1]/body[1]/div[1]/div[1]/div[2]/ul[1]/li[5]/ul[1]/li[9]/a[1]'
        self.main_steam_sign_in = "input[alt='Sign In']"
        self.main_statistics_top_cont = "li[id='nav_toplist'] li:nth-child(8) a:nth-child(1)"
        self.main_refined_metal_price = "a[href='/stats/Unique/Refined%20Metal/Tradable/Craftable']"
        self.main_key_price = "a[href='/stats/Unique/Mann%20Co.%20Supply%20Crate%20Key/Tradable/Craftable']"
        self.main_earbud_price = "a[href='/stats/Unique/Earbuds/Tradable/Craftable']"
        self.main_vm_promo_listings = "div[class='col-md-7'] div[class='panel panel-main'] div[class='panel-heading'] span[class='panel-extras'] div a[class='btn btn-panel']"
        self.main_first_item = 'body > main:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(1)'
        self.main_first_item_price = 'body > main:nth-child(10) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(2) > span:nth-child(2)'
        self.main_first_item_arrow = 'body main div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(2) div:nth-child(1) ul:nth-child(1) li:nth-child(1) div:nth-child(4) div:nth-child(1) i:nth-child(1)'
        self.main_first_item_popup_menu = ".popover"
        self.main_first_item_trade_offer = '.btn.btn-xs.btn-listing.btn-primary'
        self.main_backpack_premium_link ="a[href='/premium/subscribe']"
        self.main_vm_latest_threads = "body main[id='page-content'] div:nth-child(4) div:nth-child(1) div:nth-child(1) div:nth-child(1) span:nth-child(2) div:nth-child(1) a:nth-child(1)"
        self.main_vm_latest_news = "body main[id='page-content'] div:nth-child(4) div:nth-child(2) div:nth-child(1) div:nth-child(1) span:nth-child(2) div:nth-child(1) a:nth-child(1)"
        self.main_vm_latest_changes = "div[class='col-md-12'] div[class='panel panel-main'] div[class='panel-heading'] span[class='panel-extras'] div a[class='btn btn-panel']"
        self.main_expand_price_suggest = "a[href='/vote?sort=popular']"
        self.main_expand_recent_suggest = "body main[id='page-content'] div:nth-child(6) div:nth-child(2) div:nth-child(1) div:nth-child(1) span:nth-child(2) div:nth-child(1) a:nth-child(1)"
        self.main_footer_c_forum = 'body > footer:nth-child(9) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)'
        self.main_footer_about = "a[href='/about']"
        self.main_footer_help = "a[href='/help']"
        self.main_footer_c_rules = "a[href='/rules']"
        self.main_footer_issue_tracker = "a[href='/issues']"
        self.main_footer_dev_center = "a[href='/developer']"
        self.main_footer_pricegrid = "a[href='/pricelist']"
        self.main_footer_spreadsheet = 'body > footer:nth-child(16) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)'
        self.main_footer_unusual_by_item = 'body > footer:nth-child(15) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1)'
        self.main_footer_unusual_by_effect = 'body > footer:nth-child(15) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)'
        self.main_footer_market_pricelist = 'body > footer:nth-child(9) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(5) > a:nth-child(1)'
        self.main_footer_calc = 'body > footer:nth-child(14) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(6) > a:nth-child(1)'
        self.main_footer_vote_price = 'body > footer:nth-child(13) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)'
        self.main_footer_latest_changes = 'body > footer:nth-child(13) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)'
        self.main_footer_top_contr = 'body > footer:nth-child(15) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1)'
        self.main_footer_most_accurate = 'body > footer:nth-child(15) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)'
        self.main_footer_steamrep = "a[href='http://www.steamrep.com']"
        self.main_footer_kritzkast = "a[href='http://www.kritzkast.com/']"
        self.main_footer_scrap = "a[href='http://scrap.tf']"
        self.main_footer_rep = "a[href='https://rep.tf']"
        self.main_footer_unboxer = "a[href='https://unboxer.tf']"
        self.main_footer_dispenser = "a[href='http://dispenser.tf']"
        self.main_footer_marketplace = "a[href='https://marketplace.tf/?r=76561198045802942']"
        self.main_footer_save = "a[href='https://save.tf']"
        self.main_socials_forum = '.social-icon.fa.fa-comments-o'
        self.main_socials_discord = '.social-icon.fa.fa-commenting-o'
        self.main_socials_steam = '.social-icon.stm.stm-steam'
        self.main_socials_twitter = '.social-icon.fa.fa-twitter'
        self.main_socials_servers = '.social-icon.fa.fa-hdd-o'

        
        # Quick Functions
    def open_backpack_tf(self):
        self.sb.open(BASE_URL)
        
    def rocket_jumper_unique_search(self, item_name):
        """
        This will search the item you type and select the unique quality of that item since
        
        :return: 
        """
        self.sb.click(self.main_search_input)
        self.sb.type(self.main_search_placeholder, item_name)
        self.sb.click("//a[contains(text(),'0.11–0.16 ref')]")

    def hover_over_first_item(self):
        self.sb.hover_over_element(self.main_first_item)

    def verify_item_page(self, item_text):
        self.sb.assert_title_contains(item_text)
        self.sb.assert_element_visible('.price-boxes')
