Feature: Facebook Logo

    Scenario: Logo presence on Facebook homepage
        Given launch chrome browser
        When open facebook homepage
        Then verify that the logo present on page
        And close browser