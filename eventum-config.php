<?php
/*
 * Eventum setup for PLD Linux.
 *
 * This configuration file sets up system paths for Eventum.
 * You should not change anything in this file.
 *
 * All changes should go to %{SYSCONFDIR}%/config.php instead.
 *
 * But, if You do need to change something in this config, open bug on that in
 * http://bugs.pld-linux.org.
 */

ini_set('allow_url_fopen', 0);
ini_set('display_errors', 0);
set_time_limit(0);
set_magic_quotes_runtime(0);

// prevent session from messing up the browser cache
ini_set('session.cache_limiter', 'nocache');

// definitions of path related variables
define('APP_PATH', '%{APP_PATH}%/htdocs/');
define('APP_INC_PATH', '%{APP_PATH}%/include/');
define('APP_PEAR_PATH', '%{PHP_PEAR_DIR}%/');
define('APP_TPL_PATH', '%{APP_PATH}%/templates/');
define('APP_SMARTY_PATH', '%{SMARTY_DIR}%/');
define('APP_JPGRAPH_PATH', APP_INC_PATH . "jpgraph/");
define('APP_LOG_PATH', '/var/log/eventum/');
define('APP_LOCKS_PATH', '/var/run/eventum/');
ini_set('include_path', '.:' . APP_PEAR_PATH);

define('APP_SETUP_PATH', APP_PATH);
define('APP_SETUP_FILE', '%{SYSCONFDIR}%/setup.php');

define('APP_ERROR_LOG', APP_LOG_PATH . 'errors.log');
define('APP_CLI_LOG', APP_LOG_PATH . 'cli.log');
define('APP_IRC_LOG', APP_LOG_PATH . 'irc_bot.log');
define('APP_LOGIN_LOG', APP_LOG_PATH . 'login_attempts.log');

define('APP_VERSION', '%{APP_VERSION}%');

# include site config
include_once '%{SYSCONFDIR}%/config.php';

// define the user_id of system user
if (!defined('APP_SYSTEM_USER_ID')) {
    define('APP_SYSTEM_USER_ID', 1);
}

// if full text searching is enabled
if (!defined('APP_ENABLE_FULLTEXT')) {
    define('APP_ENABLE_FULLTEXT', false);
}

if (!defined('APP_BENCHMARK')) {
    define('APP_BENCHMARK', false);
}

if (!defined('APP_DEFAULT_ASSIGNED_EMAILS')) {
    define('APP_DEFAULT_ASSIGNED_EMAILS', 1);
}
if (!defined('APP_DEFAULT_NEW_EMAILS')) {
    define('APP_DEFAULT_NEW_EMAILS', 0);
}
if (!defined('APP_COOKIE_URL')) {
    define('APP_COOKIE_URL', APP_RELATIVE_URL);
}
if (!defined('APP_COOKIE_DOMAIN')) {
    define('APP_COOKIE_DOMAIN', APP_HOSTNAME);
}
if (!defined('APP_HASH_TYPE')) {
    define('APP_HASH_TYPE', 'MD5');
}

if (APP_BENCHMARK) {
    // always benchmark the scripts
    require_once 'Benchmark/Timer.php';
    $bench = new Benchmark_Timer;
    $bench->start();
}

include_once APP_INC_PATH . 'class.misc.php';

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
$HTTP_GET_VARS = Misc::dispelMagicQuotes($HTTP_GET_VARS);
$HTTP_POST_VARS = Misc::dispelMagicQuotes($HTTP_POST_VARS);
$_REQUEST = Misc::dispelMagicQuotes($_REQUEST);

// handle the language preferences now
include_once(APP_INC_PATH . 'class.language.php');
Language::setPreference();

// set charset
header('Content-Type: text/html; charset=' . APP_CHARSET);

/* vim: set expandtab tabstop=4 shiftwidth=4: */
?>
