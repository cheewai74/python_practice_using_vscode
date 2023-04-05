*** Settings ***
Library        SeleniumLibrary

*** Keywords ***
Begin Web Test
        #open the browser
        log                            Launching the browser
        open browser                   https://automationplayground.com/crm/    chrome 

End Web Test
...     sleep                          5s    
        close browser 