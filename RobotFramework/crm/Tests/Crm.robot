*** Settings ***
Documentation      This is some basic info about the whole suite
Library            SeleniumLibrary    

Resource           ../Resources/Common.robot
Test Setup         Begin Web Test
Test Teardown      End Web Test            

*** Variables ***
${MY VARIABLE}=    Starting the test case
@{LIST}=           one    two    three   

*** Test Cases ***
Should be able to add new customer
    [Documentation]                This is some basic info about the TEST
    [Tags]                         1006    Smoke    Contacts

    #Initialize Selenium
    Set selenium speed             .2s
    Set selenium Timeout           10s

    #open the browser
    log                            ${MY VARIABLE}
    @{alphabets}=    Create List    a    b    c
    Log    ${alphabets}
    #resize browser window for recording
    Set window position            x=341    y=169
    Set window size                width=1935    height=1090

    page should contain            Customers Are Priority One

    click link                     Sign In
    page should contain            Login

    input text                     id=email-id                                  Zebraswtestzsg711@gmail.com
    input text                     id=password                                  zebratest123  
    click button                   Submit

    page should contain            Our Happy Customers

    click link                     id=new-customer
    page should contain            Add Customer

    input text                     id=EmailAddress                              zebraswtest12@hotmail.com 
    input text                     id=FirstName                                 Software 
    input text                     id=LastName                                  Test 
    input text                     id=City                                      Dallas
    select from list by value      id=StateOrRegion                             TX   
    select radio button            gender                                       male 
    select checkbox                name=promos-name

    click button                   Submit
    wait until page contains       Success! New customer added.
 

*** Keywords ***