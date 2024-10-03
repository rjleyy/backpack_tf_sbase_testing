import pytest
from specs.bs_setup import BaseTest
from pages.main_page import MainPage


class TestMainPage(BaseTest):

    def setUp(self, masterqa_mode=False):
        super().setUp()
        self.mainpage = MainPage(self)
        self.mainpage.open_backpack_tf()

    def tearDown(self):
        print("Log Out")
        super().tearDown()


    @pytest.mark.menu_links
    def test_game_navi_icon_tf2(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_game_navi)
        self.click(mainpage.main_game_navi_tf2)
        self.assert_url('https://backpack.tf/')

    @pytest.mark.menu_links
    def test_game_navi_icon_dota_2(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_game_navi)
        self.click(mainpage.main_game_navi_dota_2)
        self.assert_url('https://dota2.backpack.tf/')

    @pytest.mark.menu_links
    def test_game_navi_icon_csgo(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_game_navi)
        self.click(mainpage.main_game_navi_csgo)
        self.assert_url('https://csgo.backpack.tf/')

    @pytest.mark.menu_links
    def test_header_forum_link(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_forum_page_link)
        self.assert_url_contains('forums')

    @pytest.mark.menu_links
    def test_main_pricegrid_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_pricing_dropdown)
        self.click(mainpage.main_pricing_pricegrid_link)
        self.assert_url('https://backpack.tf/pricelist')
        self.assert_element_visible('#page-content > div.panel.panel-main')

    @pytest.mark.menu_links
    def test_main_spreadsheet_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_pricing_dropdown)
        self.click(mainpage.main_pricing_spreadsheet_link)
        self.assert_url('https://backpack.tf/spreadsheet')
        self.assert_elements_present('.col-md-12')

    @pytest.mark.menu_links
    def test_main_browse_suggestions_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_pricing_dropdown)
        self.click(mainpage.main_pricing_suggestions_link)
        self.assert_url_contains('steamcommunity.com')

    @pytest.mark.menu_links
    def test_main_latest_changes_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_pricing_dropdown)
        self.click(mainpage.main_pricing_latest_changes_link)
        self.assert_url('https://backpack.tf/latest')
        self.assert_elements_present('.col-md-12')

    @pytest.mark.menu_links
    def test_main_unusual_items_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_pricing_dropdown)
        self.click(mainpage.main_pricing_unusual_item_link)
        self.assert_url('https://backpack.tf/unusuals')
        self.assert_elements_present('.col-md-12')
        self.assert_text_visible('Unusual Items', "div[class='row'] div[class='panel-heading'] span:nth-child(1)")

    @pytest.mark.menu_links
    def test_main_unusual_effects_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_pricing_dropdown)
        self.click(mainpage.main_pricing_unusual_effect_link)
        self.assert_url('https://backpack.tf/effects')
        self.assert_elements_present('body > main:nth-child(6) > div:nth-child(2) > div:nth-child(2)')
        self.assert_text_visible('Particle Effects', "body > main:nth-child(6) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)")




















    def test_trolldier_unique_primary(self):
        mainpage = MainPage(self)
        mainpage.item_unique_search('rocket jumper')
        self.assert_text_visible('The Rocket Jumper', '.stats-header-title')

    def test_trolldier_unique_secondary(self):
        mainpage = MainPage(self)
        mainpage.item_unique_search('mantreads')
        self.assert_title_contains('Mantreads')
