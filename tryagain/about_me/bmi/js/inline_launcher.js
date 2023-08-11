(function() {
    var self = this;
    var jquery = false;
    var nocache = false;
    var scripts, currentScript, tmp, obj, id, saObj, filelist, queue, path
    var isMobile = {
        Android: function() {
            return navigator.userAgent.match(/Android/i) ? true : false;
        },
        Tablet: function() {
            return navigator.userAgent.match(/iPad|(?!.*mobile).*Android*/i) ? true : false;
        },
        iOS: function() {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i) ? true : false;
        },
        Windows: function() {
            return navigator.userAgent.match(/IEMobile/i) ? true : false;
        },
        any: function() {
            return (isMobile.Android() || isMobile.iOS() || isMobile.Windows() || isMobile.Tablet());
        }
    };
    if (isMobile.any()) {
        nocache = true;
    }
    if (typeof window.tools == 'undefined') {
        window.tools = {};
    }
    var script = document.getElementById('tool-script_bmi')
    var path = script.src.replace('js/inline_launcher.js', '')
    this.loadAssets = function() {
        for (var key in filelist) {
            include(path + filelist[key]);
        }
        self.initQueue();
    }

    function getScript(url, success) {
        // fetch JS dependency
        var script = document.createElement('script');
        script.src = url;
        if (nocache) {
            script.src += '?nocache=' + Math.random();
        }
        var head = document.getElementsByTagName('head')[0],
            done = false;
        script.onload = script.onreadystatechange = function() {
            if (!done && (!this.readyState || this.readyState == 'loaded' || this.readyState == 'complete')) {
                done = true;
                success();
                script.onload = script.onreadystatechange = null;
                head.removeChild(script);
            };
        };
        head.appendChild(script);
    };
    this.checkJquery = function() {
        // check if jquery is present, include if not
        if (typeof jQuery == 'undefined') {
            getScript(path + 'vendor/jquery-3.2.1.min.js', function() {
                this.configure()
            });
        } else {
            this.configure()
        };
    }
    this.checkAdobeAnalytics = function() {
        // check if adobe analytics dependencies need to be acquired
        if (typeof _satellite == 'undefined' && config.adobe_analytics) {
            include('//assets.adobedtm.com/launch-ENe7f6cdd7cc05409b86547d9153429788.min.js');
        }
        self.loadAssets();
    }
    this.initQueue = function() {
        // poll environment for key dependencies before initialising
        var timer = setInterval(function() {
            if (typeof bmiIndex != 'undefined' && $ != 'undefined') {
                self.init();
                clearInterval(timer)
            }
        }, 300)
    }
    this.init = function() {
        // launch tool
        window.tools['bmi'] = new bmiIndex(path, $('#tool_bmi'), isMobile.any(), config, path);
    }
    self.configure = function() {
        // fetch the config and determine core tool variables
        var url = path + 'config.json'
        if (nocache) {
            url += '?nocache=' + Math.random();
        }
        $.getJSON(url, function(data) {
            config = data;
            config.nocache = nocache
            var framed = window.self !== window.top
            var referrer = '';
            var cross_origin = false;
            var nhs = document.location.href.indexOf('nhs.uk') > -1
            if (framed) {
                if (document.referrer != '') {
                    referrer = new URL(document.referrer).hostname
                }
                cross_origin = referrer !== new URL(document.location.href).hostname
                nhs = document.referrer.indexOf('nhs.uk') > -1
                if (document.referrer.indexOf('developer.api.nhs.uk') > -1) {
                    config.adobe_analytics = false;
                }
            }
            if (typeof NHSCookieConsent != 'undefined' && config.adobe_analytics && !framed && nhs) {
                config.adobe_analytics = NHSCookieConsent.getStatistics();
            }
            if (framed && nhs && !cross_origin) {
                config.adobe_analytics = parent.NHSCookieConsent.getStatistics();
            }
            switch (config.environment) {
                case 'production':
                    filelist = ['js/app.main.min.js', 'css/bmi-shared.css'];
                    break;
                case 'localhost':
                    filelist = ['utilities/package.php', 'css/bmi-shared.css'];
                    break;
            }
            if (isMobile.any()) {
                filelist.push('css/bmi-mobile.css')
            } else {
                filelist.push('css/bmi-desktop.css')
            }
            if (config.webtrends) {
                filelist.push('vendor/webtrends.min.js')
            }
            queue = filelist.length;
            if (framed && cross_origin && nhs && config.adobe_analytics) {
                window.addEventListener("message", function(event) {
                    config.adobe_analytics = (JSON.parse(event.data).cookie_consent)
                    self.checkAdobeAnalytics();
                }, false);
                window.parent.postMessage('{"id":"bmi","antbits_get_cookie_consent": null}', '*');

            } else {
                self.checkAdobeAnalytics();
            }

        })
    }

    function include(file, callback) {
        // load and embed JS & CSS dependencies
        var head = document.getElementsByTagName('head')[0];
        var obj
        var filetype = file.split('.').pop();
        if (nocache) {
            file += '?nocache=' + Math.random();
        }
        switch (filetype) {
            case 'css':
                obj = document.createElement('link');
                obj.type = 'text/css';
                obj.rel = 'stylesheet';
                obj.href = file;
                break;
            default:
                obj = document.createElement('script');
                obj.type = 'text/javascript';
                obj.src = file;
                break;
        }
        obj.onload = obj.onreadystatechange = function() {
            if (callback) {
                callback();
                obj.onload = null;
            }
        };
        head.appendChild(obj);
    }
    self.checkJquery()

})();