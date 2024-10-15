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
        self.assert_url("https://backpack.tf/")

    @pytest.mark.menu_links
    def test_game_navi_icon_dota_2(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_game_navi)
        self.click(mainpage.main_game_navi_dota_2)
        self.assert_url("https://dota2.backpack.tf/")

    @pytest.mark.menu_links
    def test_game_navi_icon_csgo(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_game_navi)
        self.click(mainpage.main_game_navi_csgo)
        self.assert_url("https://csgo.backpack.tf/")

    @pytest.mark.menu_links
    def test_header_forum_link(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_forum_page_link)
        self.assert_url_contains("forums")

    @pytest.mark.menu_links
    def test_main_pricegrid_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_pricing_dropdown)
        self.click(mainpage.main_pricing_pricegrid_link)
        self.assert_url("https://backpack.tf/pricelist")
        self.assert_element_visible("#page-content > div.panel.panel-main")

    @pytest.mark.menu_links
    def test_main_spreadsheet_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_pricing_dropdown)
        self.click(mainpage.main_pricing_spreadsheet_link)
        self.assert_url("https://backpack.tf/spreadsheet")
        self.assert_elements_present(".col-md-12")

    @pytest.mark.menu_links
    def test_main_browse_suggestions_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_pricing_dropdown)
        self.click(mainpage.main_pricing_suggestions_link)
        self.assert_url_contains("steamcommunity.com")

    @pytest.mark.menu_links
    def test_main_latest_changes_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_pricing_dropdown)
        self.click(mainpage.main_pricing_latest_changes_link)
        self.assert_url("https://backpack.tf/latest")
        self.assert_elements_present(".col-md-12")

    @pytest.mark.menu_links
    def test_main_unusual_items_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_pricing_dropdown)
        self.click(mainpage.main_pricing_unusual_item_link)
        self.assert_url("https://backpack.tf/unusuals")
        self.assert_elements_present(".col-md-12")
        self.assert_text_visible(
            "Unusual Items",
            "div[class='row']" " div[class='panel-heading'] span:nth-child(1)",
        )

    @pytest.mark.menu_links
    def test_main_unusual_effects_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_pricing_dropdown)
        self.click(mainpage.main_pricing_unusual_effect_link)
        self.assert_url("https://backpack.tf/effects")
        self.assert_elements_present(
            "body > main:nth-child(6) > div:nth-child(2) > div:nth-child(2)"
        )
        self.assert_text_visible(
            "Particle Effects",
            "body > main:nth-child(6) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
        )

    @pytest.mark.menu_links
    def test_main_classified_listings_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_trading_dropdown)
        self.click(mainpage.main_trading_classified)
        self.assert_url("https://backpack.tf/classifieds")

    @pytest.mark.menu_links
    def test_main_calculator_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_trading_dropdown)
        self.click(mainpage.main_trading_calc)
        self.assert_url("https://backpack.tf/calculator")
        self.assert_elements(
            "a[id='calc-new'] span[class='hidden-xs']",
            "a[id='calc-open'] span[class='hidden-xs']",
            "a[id='calc-save'] span[class='hidden-xs']",
            "a[id='calc-share'] span[class='hidden-xs']",
        )

    @pytest.mark.menu_links
    def test_main_premium_listing_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_trading_dropdown)
        self.click(mainpage.main_trading_premium)
        self.assert_url_contains("steamcommunity")

    @pytest.mark.menu_links
    def test_main_browse_items_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_statistics_dropdown)
        self.click(mainpage.main_statistics_browse_items)
        self.assert_url("https://backpack.tf/stats")
        self.assert_elements_present(".stats-breadcrumbs")

    @pytest.mark.menu_links
    def test_main_top_inventory_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_statistics_dropdown)
        self.click(mainpage.main_statistics_top_inv)
        self.assert_url("https://backpack.tf/top/backpacks")
        self.assert_text_visible("last updated")

    @pytest.mark.menu_links
    def test_main_top_donators_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_statistics_dropdown)
        self.click(mainpage.main_statistics_top_dono)
        self.assert_url("https://backpack.tf/top/donators")
        self.assert_link_text("clicking here")
        self.click("a[href='/donate']")
        self.assert_url("https://backpack.tf/donate")

    @pytest.mark.menu_links
    def test_main_top_gifters_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_statistics_dropdown)
        self.click(mainpage.main_statistics_top_gift)
        self.assert_url("https://backpack.tf/top/generous")
        self.assert_text(
            "These users gave out the most months of Premium to different users."
        )

    @pytest.mark.menu_links
    def test_main_top_contributors_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_statistics_dropdown)
        self.click(mainpage.main_statistics_top_cont)
        self.assert_url("https://backpack.tf/top/contributors")
        self.assert_text("Top Contributors This thing ain't on auto-pilot, son!")

    @pytest.mark.menu_links
    def test_main_most_accurate_link(self):
        mainpage = MainPage(self)
        self.hover_over_element(mainpage.main_statistics_dropdown)
        self.click(mainpage.main_statistics_most_accurate)
        self.assert_url("https://backpack.tf/top/accurate")
        self.assert_text_visible(
            "Previous Month's Most Accurate Users With 50 votes minimum"
        )

    @pytest.mark.menu_links
    def test_main_steam_sign_in_link(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_steam_sign_in)
        self.assert_url_contains("steamcommunity")

    @pytest.mark.menu_links
    def test_main_refined_price_link(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_refined_metal_price)
        mainpage.verify_item_page("Refined Metal")

    @pytest.mark.menu_links
    def test_main_key_price_link(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_key_price)
        mainpage.verify_item_page("Mann Co. Supply Crate Key")

    @pytest.mark.menu_links
    def test_main_earbud_price_link(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_earbud_price)
        mainpage.verify_item_page("Earbuds")

    @pytest.mark.menu_links
    def test_promo_listing_updating(self):
        mainpage = MainPage(self)
        mainpage.hover_over_first_item()
        original_item = self.get_text(".popover-title")
        self.sleep(45)
        self.refresh()
        mainpage.hover_over_first_item()
        self.assert_element_not_visible(original_item)

    @pytest.mark.menu_links
    def test_premium_offer_link(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_backpack_premium_link)
        self.assert_url("https://backpack.tf/premium/subscribe")

    @pytest.mark.menu_links
    def test_view_more_threads(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_vm_latest_threads)
        self.assert_url("https://forums.backpack.tf/")

    @pytest.mark.menu_links
    def test_view_more_news(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_vm_latest_news)
        self.assert_url("https://steamcommunity.com/groups/meetthestats")

    @pytest.mark.menu_links
    def test_view_more_changes(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_vm_latest_changes)
        self.assert_url("https://backpack.tf/latest")

    @pytest.mark.menu_links
    def test_expand_active_price_suggestions(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_expand_price_suggest)
        self.assert_url_contains("steamcommunity")

    @pytest.mark.menu_links
    def test_expand_recent_price_suggestions(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_expand_recent_suggest)
        self.assert_url_contains("steamcommunity")

    @pytest.mark.menu_links
    def test_footer_forum(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_c_forum)
        self.assert_url("https://forums.backpack.tf/")

    @pytest.mark.menu_links
    def test_footer_about(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_about)
        self.assert_url("https://backpack.tf/about")

    @pytest.mark.menu_links
    def test_footer_help(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_help)
        self.assert_url("https://backpack.tf/help")

    @pytest.mark.menu_links
    def test_footer_community_rules(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_c_rules)
        self.assert_url("https://backpack.tf/rules")

    @pytest.mark.menu_links
    def test_footer_issue_tracker(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_issue_tracker)
        self.assert_url("https://backpack.tf/issues")

    @pytest.mark.menu_links
    def test_footer_developer_center(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_dev_center)
        self.assert_url("https://backpack.tf/developer")

    @pytest.mark.menu_links
    def test_footer_pricegrid(self):
        self.click_link_text("Pricegrid")
        self.assert_url("https://backpack.tf/pricelist")

    @pytest.mark.menu_links
    def test_footer_spreadsheet(self):
        self.click_link_text("Spreadsheet")
        self.assert_url("https://backpack.tf/spreadsheet")

    @pytest.mark.menu_links
    def test_footer_unusual_by_item(self):
        self.click_link_text("Unusuals by Item")
        self.assert_url("https://backpack.tf/unusuals")

    @pytest.mark.menu_links
    def test_footer_unusual_by_effect(self):
        self.click_link_text("Unusuals by Effect")
        self.assert_url("https://backpack.tf/effects")

    @pytest.mark.menu_links
    def test_footer_market_pricelist(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_market_pricelist)
        self.assert_url("https://backpack.tf/market")

    @pytest.mark.menu_links
    def test_footer_calculator(self):
        self.click_link_text("Calculator")
        self.assert_url("https://backpack.tf/calculator")

    @pytest.mark.menu_links
    def test_footer_votes_on_prices(self):
        self.click_link_text("Vote on prices")
        self.assert_url_contains("steamcommunity")

    @pytest.mark.menu_links
    def test_footer_latest_changes(self):
        self.click_link_text("Latest changes")
        self.assert_url("https://backpack.tf/latest")

    @pytest.mark.menu_links
    def test_footer_top_contributors(self):
        self.click_link_text("Top contributors")
        self.assert_url("https://backpack.tf/top/contributors")

    @pytest.mark.menu_links
    def test_footer_most_accurate(self):
        self.click_link_text("Most accurate")
        self.assert_url("https://backpack.tf/top/accurate")

    # This test cannot be automated because Steamrep runs a human verification check everytime the url loads
    # @pytest.mark.menu_links
    # def test_footer_steamrep(self):
    #    self.click(mainpage.main_footer_steamrep)
    #    self.assert_url('https://steamrep.com/')

    @pytest.mark.menu_links
    def test_footer_kritzkast(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_kritzkast)
        self.assert_url("https://kritzkast.com/")

    @pytest.mark.menu_links
    def test_footer_scraptf(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_scrap)
        self.assert_url("https://scrap.tf/")

    @pytest.mark.menu_links
    def test_footer_reptf(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_rep)
        self.assert_url("https://rep.tf/")

    @pytest.mark.menu_links
    def test_footer_unboxertf(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_unboxer)
        self.assert_url("https://unboxer.tf/")

    @pytest.mark.menu_links
    def test_footer_dispensertf(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_dispenser)
        self.assert_url("https://dispenser.tf/")

    @pytest.mark.menu_links
    def test_footer_marketplacetf(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_marketplace)
        self.assert_url_contains("https://marketplace.tf/")

    @pytest.mark.menu_links
    def test_footer_savetf(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_footer_save)
        self.assert_url("https://save.tf/")

    @pytest.mark.menu_links
    def test_socials_forum(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_socials_forum)
        self.assert_url("https://forums.backpack.tf/")

    # This test also has a human verification check but the url is the same.
    @pytest.mark.menu_links
    def test_socials_discord(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_socials_discord)
        self.assert_url("https://discord.backpack.tf/")

    @pytest.mark.menu_links
    def test_socials_steam(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_socials_steam)
        self.assert_url_contains("steamcommunity")

    @pytest.mark.menu_links
    def test_socials_twitter(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_socials_twitter)
        self.assert_url_contains("x.com/backpacktf")

    @pytest.mark.menu_links
    def test_socials_servers(self):
        mainpage = MainPage(self)
        self.click(mainpage.main_socials_servers)
        self.assert_url("https://backpack.tf/servers")
