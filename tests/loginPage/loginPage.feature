Feature: User logs in to the website

  Scenario Outline: Outlined given, when & then
    Given user provides <username> and <password>
    When user clicks on Login Button
    Then result page should have <xpath> containing <text>

    Examples: Data Combinations
      | username      | password     | xpath                                         | text                                                        |
      | standard_user | secret_sauce | //*[@id="inventory_filter_container"]/div     | Products                                                    |
      | standard_user | wrong_pass   | //*[@id="login_button_container"]/div/form/h3 | Username and password do not match any user in this service |
      | wrong_user    | wrong_pass   | //*[@id="login_button_container"]/div/form/h3 | Username and password do not match any user in this service |
      | standard_user |              | //*[@id="login_button_container"]/div/form/h3 | Password is required                                        |