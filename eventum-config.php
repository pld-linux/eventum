<?php
/*
 * Eventum setup for PLD Linux.
 *
 * This configuration file sets up system paths for eventum.
 * You shouldn't be needing to change anything in this file.
 * All changes should go to /etc/eventum/config.php
 * But, if You do need to change something in this config, please let us know!
 */

ini_set('allow_url_fopen', 0);
ini_set("display_errors", 0);
error_reporting(0);
set_time_limit(0);
// prevent session from messing up the browser cache
ini_set('session.cache_limiter', 'nocache');

// definitions of path related variables
@define("APP_PATH", '/usr/share/eventum/');
@define("APP_INC_PATH", APP_PATH . "include/");
@define("APP_PEAR_PATH", APP_INC_PATH . "pear/");
@define("APP_TPL_PATH", APP_PATH . "templates/");
@define("APP_SMARTY_PATH", "/usr/share/pear/Smarty/");
@define("APP_JPGRAPH_PATH", APP_INC_PATH . "jpgraph/");
@define("APP_LOG_PATH", "/var/log/eventum/");
@define("APP_LOCKS_PATH", "/var/run/eventum/");
ini_set("include_path", ".:" . APP_PEAR_PATH);

@define("APP_SETUP_PATH", APP_PATH);
@define("APP_SETUP_FILE", APP_SETUP_PATH . "setup.conf.php");

@define("APP_ERROR_LOG", APP_LOG_PATH . "errors.log");
@define("APP_CLI_LOG", APP_LOG_PATH . "cli.log");
@define("APP_IRC_LOG", APP_LOG_PATH . "irc_bot.log");
@define("APP_LOGIN_LOG", APP_LOG_PATH . "login_attempts.log");

@define("APP_VERSION", "%{APP_VERSION}%");

// define the user_id of system user
@define("APP_SYSTEM_USER_ID", 1);

@define("APP_BENCHMARK", false);

# include site config
include_once '/etc/eventum/config.php';

if (APP_BENCHMARK) {
    // always benchmark the scripts
    include_once("Benchmark/Timer.php");
    $bench = new Benchmark_Timer;
    $bench->start();
}

include_once(APP_INC_PATH . "class.misc.php");

if (isset($_GET)) {
    $HTTP_POST_VARS = $_POST;
    $HTTP_GET_VARS = $_GET;
    $HTTP_SERVER_VARS = $_SERVER;
    $HTTP_ENV_VARS = $_ENV;
    $HTTP_POST_FILES = $_FILES;
    // seems like PHP 4.1.0 didn't implement the $_SESSION auto-global...
    if (isset($_SESSION)) {
        $HTTP_SESSION_VARS = $_SESSION;
    }
    $HTTP_COOKIE_VARS = $_COOKIE;
}

// fix magic_quote_gpc'ed values (i wish i knew who is the person behind this)
$HTTP_GET_VARS =& Misc::dispelMagicQuotes($HTTP_GET_VARS);
$HTTP_POST_VARS =& Misc::dispelMagicQuotes($HTTP_POST_VARS);

// handle the language preferences now
@include_once(APP_INC_PATH . "class.language.php");
Language::setPreference();

// set charset
header("Content-Type: text/html; charset=" . APP_CHARSET);

/* vim: set expandtab tabstop=4 shiftwidth=4: */
?>
