Using step definitions from: 'steps'

Feature: Show that using the ConfigReader generates the expected results

    Scenario: Show that loading a configuration file succeeds
        Given a configuration file: test.cfg
        When the configuration file is loaded no errors are thrown

    Scenario: Show that ConfigReader finds all the expected sections
        Given a configuration file: test.cfg
        When the configuration file is loaded no errors are thrown
        Then the sections should be: TYPES,DEFAULT,test,testnames

    Scenario Outline: Show that the following Section/Key pairs match the file
        Given a configuration file: test.cfg
        When the configuration file is loaded no errors are thrown
        Then <section>, should have a key: <key> which equals: <value>
        Examples:
            | section   | key       | value             |
            | TYPES     | default   | string            |
            | TYPES     | a         | int               |
            | DEFAULT   | fname     | Elvis             |
            | DEFAULT   | lname     | Pressley          |
            | test      | a         | 1                 |
            | test      | b         | 2                 |
            | testnames | t1        | This is a test    |

    Scenario: Show that ConfigReader handles item resolution correctly
        Given a configuration file: test.cfg
        When the configuration file is loaded no errors are thrown
        Then DEFAULT, should have a key: name which equals: Pressley, Elvis
