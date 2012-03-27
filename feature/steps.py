from freshen import *
from freshen.checks import *
import os

import ReadConfig

@Before
def before(sc):
    try:
        scc.config = ReadConfig.ReadConfig()
    except:
        raise StandardError("Couldn't create the object...")

@After
def after(sc):
    del(scc.config)
 
@Given("a configuration file: (\w+.*)")
def getConfig(configfile):
    if os.path.isfile(configfile.strip()):
        scc.config_file = configfile.strip()
    else:
        raise StandardError("Didn't find: '%s'" % (configfile.strip()))

@Then("the sections should be: (\w+.*)")
def checkSections(data):
    assert_true(scc.config.get_sections() == map(lambda x: x.strip(), data.split(",")), 
            "'%s' didn't match '%s'" % (scc.config.get_sections(), map(lambda x: x.strip(), data.split(","))))


@Then("(\w+.*), should have a key: (\w+.*) which equals: (\w+.*)")
def checkValues(section, key, value):
    assert_true(scc.config[section.strip()][key.strip()] == value.strip(),
            "'%s' didn't match '%s'" % (scc.config[section.strip()][key.strip()], value.strip()))

@When("the configuration file is loaded no errors are thrown")
def loadConfig():
    try:
        scc.config.read(scc.config_file)
    except:
        raise StandardError("Loading the file failed")
