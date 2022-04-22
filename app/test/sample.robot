*** Settings ***
Library   Browser
Library   config.py
Library   defect.py

*** Test Cases ***
Example Test
    ${value}    Capability
    Log         ${value}
    Connect To Browser    wss://cdp.lambdatest.com/playwright?capabilities=${value}    chromium   
    New Page    https://playwright.dev
    Get Text    h1    ==    Playwright enables reliable end-to-end testing for modern we apps.
    
   