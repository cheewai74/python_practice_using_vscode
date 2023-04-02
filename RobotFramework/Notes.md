https://robocorp.com/docs/languages-and-frameworks/robot-framework/cheat-sheet
https://automationplayground.com/


Robot Framework Project Structure:
/Tests: Test Script (.robot)
/Resources: Page Object and App Keyword File (.robot)
/Python: Selenium Library and Database Library
c:\bin: Selenium Webdrivers

/ProjectBase
    /Tests
    /Resources
        ProductApp.robot
        /PO
    /Results


    robot -d results tests/crm.robot