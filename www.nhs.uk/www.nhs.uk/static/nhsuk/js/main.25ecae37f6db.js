! function(n) {
    var r = {};

    function o(e) {
        if (r[e]) return r[e].exports;
        var t = r[e] = {
            i: e,
            l: !1,
            exports: {}
        };
        return n[e].call(t.exports, t, t.exports, o), t.l = !0, t.exports
    }
    o.m = n, o.c = r, o.d = function(e, t, n) {
        o.o(e, t) || Object.defineProperty(e, t, {
            enumerable: !0,
            get: n
        })
    }, o.r = function(e) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }), Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }, o.t = function(t, e) {
        if (1 & e && (t = o(t)), 8 & e) return t;
        if (4 & e && "object" == typeof t && t && t.__esModule) return t;
        var n = Object.create(null);
        if (o.r(n), Object.defineProperty(n, "default", {
                enumerable: !0,
                value: t
            }), 2 & e && "string" != typeof t)
            for (var r in t) o.d(n, r, function(e) {
                return t[e]
            }.bind(null, r));
        return n
    }, o.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e.default
        } : function() {
            return e
        };
        return o.d(t, "a", t), t
    }, o.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }, o.p = "", o(o.s = 7)
}([function(e, t) {
    e.exports = function(e) {
        return e.webpackPolyfill || (e.deprecate = function() {}, e.paths = [], e.children || (e.children = []), Object.defineProperty(e, "loaded", {
            enumerable: !0,
            get: function() {
                return e.l
            }
        }), Object.defineProperty(e, "id", {
            enumerable: !0,
            get: function() {
                return e.i
            }
        }), e.webpackPolyfill = 1), e
    }
}, function(e, s, t) {
    ! function(e) {
        var t;

        function n(t, e) {
            var n, r = Object.keys(t);
            return Object.getOwnPropertySymbols && (n = Object.getOwnPropertySymbols(t), e && (n = n.filter(function(e) {
                return Object.getOwnPropertyDescriptor(t, e).enumerable
            })), r.push.apply(r, n)), r
        }

        function j(r) {
            for (var e = 1; e < arguments.length; e++) {
                var o = null != arguments[e] ? arguments[e] : {};
                e % 2 ? n(Object(o), !0).forEach(function(e) {
                    var t, n;
                    t = r, n = o[e = e], e in t ? Object.defineProperty(t, e, {
                        value: n,
                        enumerable: !0,
                        configurable: !0,
                        writable: !0
                    }) : t[e] = n
                }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(r, Object.getOwnPropertyDescriptors(o)) : n(Object(o)).forEach(function(e) {
                    Object.defineProperty(r, e, Object.getOwnPropertyDescriptor(o, e))
                })
            }
            return r
        }

        function L(e, t) {
            if ("function" != typeof t && null !== t) throw new TypeError("Super expression must either be null or a function");
            e.prototype = Object.create(t && t.prototype, {
                constructor: {
                    value: e,
                    writable: !0,
                    configurable: !0
                }
            }), Object.defineProperty(e, "prototype", {
                writable: !1
            }), t && r(e, t)
        }

        function r(e, t) {
            return (r = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(e, t) {
                return e.__proto__ = t, e
            })(e, t)
        }

        function N(n) {
            var r = function() {
                if ("undefined" == typeof Reflect || !Reflect.construct) return !1;
                if (Reflect.construct.sham) return !1;
                if ("function" == typeof Proxy) return !0;
                try {
                    return Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function() {})), !0
                } catch (e) {
                    return !1
                }
            }();
            return function() {
                var e, t = o(n),
                    t = (e = r ? (e = o(this).constructor, Reflect.construct(t, arguments, e)) : t.apply(this, arguments), this);
                if (!e || "object" !== a(e) && "function" != typeof e) {
                    if (void 0 !== e) throw new TypeError("Derived constructors may only return object or undefined");
                    if (void 0 === (e = t)) throw new ReferenceError("this hasn't been initialised - super() hasn't been called")
                }
                return e
            }
        }

        function o(e) {
            return (o = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(e) {
                return e.__proto__ || Object.getPrototypeOf(e)
            })(e)
        }

        function P(e, t) {
            if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function")
        }

        function i(e, t) {
            for (var n = 0; n < t.length; n++) {
                var r = t[n];
                r.enumerable = r.enumerable || !1, r.configurable = !0, "value" in r && (r.writable = !0), Object.defineProperty(e, r.key, r)
            }
        }

        function I(e, t, n) {
            t && i(e.prototype, t), n && i(e, n), Object.defineProperty(e, "prototype", {
                writable: !1
            })
        }

        function a(e) {
            return (a = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                return typeof e
            } : function(e) {
                return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
            })(e)
        }
        window, t = function() {
            return n = [function(e, t) {
                e.exports = '<div class="nhsuk-card nhsuk-u-reading-width">\n  <div class="nhsuk-card__content">\n    <h2 class="nhsuk-card__heading nhsuk-heading-s">\n      Did this information help you?\n    </h2>\n    <ul class="nhsuk-list nhsuk-user-feedback-form">\n      <li class="nhsuk-user-feedback-form__list-item nhsuk-u-margin-bottom-0">\n        <button class="nhsuk-button nhsuk-button--secondary nhsuk-u-margin-right-4 nhsuk-u-margin-bottom-0 nhsuk-user-feedback-form--yes">\n          Yes <span class="nhsuk-u-visually-hidden">this information helped me</span>\n        </button>\n      </li>\n      <li class="nhsuk-user-feedback-form__list-item nhsuk-u-margin-bottom-0">\n        <button class="nhsuk-button nhsuk-button--secondary nhsuk-u-margin-bottom-0 nhsuk-user-feedback-form--no">\n          No <span class="nhsuk-u-visually-hidden">this information did not help me</span>\n        </button>\n      </li>\n    </ul>\n  </div>\n</div>\n'
            }, function(e, t) {
                e.exports = '<div class="nhsuk-card nhsuk-u-reading-width">\n  <div class="nhsuk-card__content">\n    <h2 class="nhsuk-card__heading nhsuk-heading-s">\n      Thank you, your feedback has been recorded\n    </h2>\n    <hr class="nhsuk-u-margin-top-0 nhsuk-u-margin-bottom-4">\n    <div class="nhsuk-form-group">\n      <label class="nhsuk-label" for="more-detail">\n        {{ label }} (optional)\n      </label>\n      <span class="nhsuk-hint nhsuk-u-margin-bottom-4" id="more-detail-hint">\n        Do not include personal information.\n      </span>\n      <textarea class="nhsuk-textarea" id="more-detail" name="more-detail" rows="5" aria-describedby="more-detail-hint"></textarea>\n    </div>\n    <button class="nhsuk-button nhsuk-button--secondary nhsuk-user-feedback-form--submit" type="submit">\n      Submit\n    </button>\n  </div>\n</div>\n'
            }, function(e, t) {
                e.exports = '<div class="nhsuk-card nhsuk-u-reading-width">\n  <div class="nhsuk-card__content">\n    <h2 class="nhsuk-card__heading nhsuk-user-feedback-form-header nhsuk-heading-s">\n      Thank you for your feedback.\n    </h2>\n      {{ optionalTextResponseMessage }}\n    <p>Find out how to <a href="/contact-us/">contact the NHS</a> if you need to speak to someone.</p>\n  </div>\n</div>\n'
            }, function(e, t, n) {
                "use strict";
                e.exports = function(i) {
                    var u = [];
                    return u.toString = function() {
                        return this.map(function(e) {
                            n = e[1] || "";
                            var t, n, r, o = (r = e[3]) ? i && "function" == typeof btoa ? (t = btoa(unescape(encodeURIComponent(JSON.stringify(r)))), t = "sourceMappingURL=data:application/json;charset=utf-8;base64,".concat(t), t = "/*# ".concat(t, " */"), o = r.sources.map(function(e) {
                                return "/*# sourceURL=".concat(r.sourceRoot || "").concat(e, " */")
                            }), [n].concat(o).concat([t]).join("\n")) : [n].join("\n") : n;
                            return e[2] ? "@media ".concat(e[2], " {").concat(o, "}") : o
                        }).join("")
                    }, u.i = function(e, t, n) {
                        "string" == typeof e && (e = [
                            [null, e, ""]
                        ]);
                        var r = {};
                        if (n)
                            for (var o = 0; o < this.length; o++) {
                                var i = this[o][0];
                                null != i && (r[i] = !0)
                            }
                        for (var a = 0; a < e.length; a++) {
                            var s = [].concat(e[a]);
                            n && r[s[0]] || (t && (s[2] ? s[2] = "".concat(t, " and ").concat(s[2]) : s[2] = t), u.push(s))
                        }
                    }, u
                }
            }, function(e, t, n) {
                e.exports = n(8)
            }, function(e, t, n) {
                var r = n(6),
                    n = n(7);
                r(n = "string" == typeof(n = n.__esModule ? n.default : n) ? [
                    [e.i, n, ""]
                ] : n, {
                    insert: "head",
                    singleton: !1
                }), e.exports = n.locals || {}
            }, function(e, t, o) {
                "use strict";
                r = {};
                var n, r, i = function(e) {
                        if (void 0 === r[e]) {
                            var t = document.querySelector(e);
                            if (window.HTMLIFrameElement && t instanceof window.HTMLIFrameElement) try {
                                t = t.contentDocument.head
                            } catch (e) {
                                t = null
                            }
                            r[e] = t
                        }
                        return r[e]
                    },
                    c = [];

                function l(e) {
                    for (var t = -1, n = 0; n < c.length; n++)
                        if (c[n].identifier === e) {
                            t = n;
                            break
                        }
                    return t
                }

                function s(e, t) {
                    for (var n = {}, r = [], o = 0; o < e.length; o++) {
                        var i = e[o],
                            a = t.base ? i[0] + t.base : i[0],
                            s = n[a] || 0,
                            u = "".concat(a, " ").concat(s),
                            a = (n[a] = s + 1, l(u)),
                            s = {
                                css: i[1],
                                media: i[2],
                                sourceMap: i[3]
                            }; - 1 !== a ? (c[a].references++, c[a].updater(s)) : c.push({
                            identifier: u,
                            updater: function(t, e) {
                                var n, r, o; {
                                    var i;
                                    o = e.singleton ? (i = h++, n = p = p || d(e), r = f.bind(null, n, i, !1), f.bind(null, n, i, !0)) : (n = d(e), r = function(e, t, n) {
                                        var r = n.css,
                                            o = n.media,
                                            n = n.sourceMap;
                                        if (o ? e.setAttribute("media", o) : e.removeAttribute("media"), n && "undefined" != typeof btoa && (r += "\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(n)))), " */")), e.styleSheet) e.styleSheet.cssText = r;
                                        else {
                                            for (; e.firstChild;) e.removeChild(e.firstChild);
                                            e.appendChild(document.createTextNode(r))
                                        }
                                    }.bind(null, n, e), function() {
                                        var e;
                                        null !== (e = n).parentNode && e.parentNode.removeChild(e)
                                    })
                                }
                                return r(t),
                                    function(e) {
                                        e ? e.css === t.css && e.media === t.media && e.sourceMap === t.sourceMap || r(t = e) : o()
                                    }
                            }(s, t),
                            references: 1
                        }), r.push(u)
                    }
                    return r
                }

                function d(e) {
                    var t = document.createElement("style"),
                        n = e.attributes || {};
                    if (void 0 !== n.nonce || (r = o.nc) && (n.nonce = r), Object.keys(n).forEach(function(e) {
                            t.setAttribute(e, n[e])
                        }), "function" == typeof e.insert) e.insert(t);
                    else {
                        var r = i(e.insert || "head");
                        if (!r) throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");
                        r.appendChild(t)
                    }
                    return t
                }
                var a;
                a = [];

                function f(e, t, n, r) {
                    var n = n ? "" : r.media ? "@media ".concat(r.media, " {").concat(r.css, "}") : r.css;
                    e.styleSheet ? e.styleSheet.cssText = (a[t] = n, a.filter(Boolean).join("\n")) : (r = document.createTextNode(n), (n = e.childNodes)[t] && e.removeChild(n[t]), n.length ? e.insertBefore(r, n[t]) : e.appendChild(r))
                }
                var p = null,
                    h = 0;
                e.exports = function(e, i) {
                    (i = i || {}).singleton || "boolean" == typeof i.singleton || (i.singleton = n = void 0 === n ? Boolean(window && document && document.all && !window.atob) : n);
                    var a = s(e = e || [], i);
                    return function(e) {
                        if (e = e || [], "[object Array]" === Object.prototype.toString.call(e)) {
                            for (var t = 0; t < a.length; t++) {
                                var n = l(a[t]);
                                c[n].references--
                            }
                            for (var e = s(e, i), r = 0; r < a.length; r++) {
                                var o = l(a[r]);
                                0 === c[o].references && (c[o].updater(), c.splice(o, 1))
                            }
                            a = e
                        }
                    }
                }
            }, function(e, t, n) {
                "use strict";
                n.r(t);
                var r = n(3),
                    n = n.n(r)()(!1);
                n.push([e.i, ".nhsuk-user-feedback-form {\n  line-height: 0;\n}\n\n.nhsuk-user-feedback-form__list-item {\n  display: inline-block;\n}\n", ""]), t.default = n
            }, function(e, t, n) {
                "use strict";
                n.r(t), "remove" in Element.prototype || (Element.prototype.remove = function() {
                    this.parentNode && this.parentNode.removeChild(this)
                }), "forEach" in NodeList.prototype || (NodeList.prototype.forEach = Array.prototype.forEach);
                I(y, [{
                    key: "updateHtml",
                    value: function(e) {
                        this.app.container.childNodes.forEach(function(e) {
                            e.remove()
                        });
                        var t = document.createElement("div");
                        return t.className = "nhsuk-user-feedback-form", t.innerHTML = e, this.app.container.appendChild(t), t
                    }
                }]);
                var i, r, o, a, s = y,
                    u = n(0),
                    c = n.n(u),
                    l = (L(b, s), a = N(b), I(b, [{
                        key: "onYes",
                        value: function() {
                            this.app.onYes()
                        }
                    }, {
                        key: "onNo",
                        value: function() {
                            this.app.onNo()
                        }
                    }, {
                        key: "addListeners",
                        value: function(e) {
                            e.querySelector(".nhsuk-user-feedback-form--yes").addEventListener("click", this.onYes.bind(this)), e.querySelector(".nhsuk-user-feedback-form--no").addEventListener("click", this.onNo.bind(this))
                        }
                    }, {
                        key: "render",
                        value: function() {
                            var e = this.updateHtml(c.a);
                            this.addListeners(e)
                        }
                    }]), b),
                    u = n(1),
                    d = n.n(u),
                    f = (L(v, s), o = N(v), I(v, [{
                        key: "getInitialQuestionResponse",
                        value: function() {
                            return this.app.isSatisfiedResponse
                        }
                    }, {
                        key: "onSubmit",
                        value: function(e) {
                            e = e.substr(0, 1e3);
                            this.app.onTextSubmit(e)
                        }
                    }, {
                        key: "addListeners",
                        value: function(t) {
                            var n = this;
                            t.querySelector(".nhsuk-user-feedback-form--submit").addEventListener("click", function() {
                                var e = t.querySelector("textarea");
                                n.onSubmit(e.value)
                            })
                        }
                    }, {
                        key: "render",
                        value: function() {
                            var e = this.getInitialQuestionResponse() ? "What happened to make you visit the NHS website today?" : "What were you looking for?",
                                e = d.a.replace("{{ label }}", e),
                                e = this.updateHtml(e);
                            e.querySelector("#more-detail").focus(), this.addListeners(e)
                        }
                    }]), v),
                    u = n(2),
                    p = n.n(u),
                    h = (L(m, s), r = N(m), I(m, [{
                        key: "getEnableTextResponse",
                        value: function() {
                            return this.app.enableTextResponse
                        }
                    }, {
                        key: "render",
                        value: function() {
                            var e = !1 === this.getEnableTextResponse() ? "" : "<p>We do not check feedback every day and cannot respond to comments.</p>",
                                e = p.a.replace("{{ optionalTextResponseMessage }}", e),
                                e = this.updateHtml(e).querySelector(".nhsuk-user-feedback-form-header");
                            e.setAttribute("tabIndex", "-1"), e.focus()
                        }
                    }]), m);

                function m() {
                    return P(this, m), r.apply(this, arguments)
                }

                function v() {
                    return P(this, v), o.apply(this, arguments)
                }

                function b() {
                    return P(this, b), a.apply(this, arguments)
                }

                function y(e) {
                    if (P(this, y), this.constructor === y) throw new TypeError("Abstract class `Screen` cannot be instantiated directly.");
                    if (void 0 === this.render) throw new TypeError("Clases extending `Screen` should define a `render` method");
                    this.app = e
                }

                function g(e, t) {
                    t = new CustomEvent("onFeedback", {
                        detail: {
                            isSatisfied: t
                        }
                    });
                    e.dispatchEvent(t)
                }
                "function" != typeof window.CustomEvent && (window.CustomEvent = function(e, t) {
                    t = t || {
                        bubbles: !1,
                        cancelable: !1,
                        detail: null
                    };
                    var n = document.createEvent("CustomEvent");
                    return n.initCustomEvent(e, t.bubbles, t.cancelable, t.detail), n
                });
                var w = new Uint8Array(16);
                for (var _ = /^(?:[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}|00000000-0000-0000-0000-000000000000)$/i, k = function(e) {
                        return "string" == typeof e && _.test(e)
                    }, S = [], E = 0; E < 256; ++E) S.push((E + 256).toString(16).substr(1));

                function x(e, t, n) {
                    var r = (e = e || {}).random || (e.rng || function() {
                        if (i = i || "undefined" != typeof crypto && crypto.getRandomValues && crypto.getRandomValues.bind(crypto) || "undefined" != typeof msCrypto && "function" == typeof msCrypto.getRandomValues && msCrypto.getRandomValues.bind(msCrypto)) return i(w);
                        throw new Error("crypto.getRandomValues() not supported. See https://github.com/uuidjs/uuid#getrandomvalues-not-supported")
                    })();
                    if (r[6] = 15 & r[6] | 64, r[8] = 63 & r[8] | 128, t) {
                        n = n || 0;
                        for (var o = 0; o < 16; ++o) t[n + o] = r[o];
                        return t
                    }
                    return function(e, t) {
                        t = 1 < arguments.length && void 0 !== t ? t : 0, e = (S[e[t + 0]] + S[e[t + 1]] + S[e[t + 2]] + S[e[t + 3]] + "-" + S[e[t + 4]] + S[e[t + 5]] + "-" + S[e[t + 6]] + S[e[t + 7]] + "-" + S[e[t + 8]] + S[e[t + 9]] + "-" + S[e[t + 10]] + S[e[t + 11]] + S[e[t + 12]] + S[e[t + 13]] + S[e[t + 14]] + S[e[t + 15]]).toLowerCase();
                        if (k(e)) return e;
                        throw TypeError("Stringified UUID is invalid")
                    }(r)
                }
                I(C, [{
                    key: "getEndpoint",
                    value: function() {
                        return this.endpoint
                    }
                }, {
                    key: "getUrl",
                    value: function() {
                        return this.currentUrl
                    }
                }, {
                    key: "post",
                    value: function(e, t) {
                        var n = new XMLHttpRequest,
                            e = this.getEndpoint() + e,
                            e = (n.open("POST", e), n.setRequestHeader("Content-Type", "application/json;charset=UTF-8"), j({}, t));
                        this.token && (e.token = this.token), n.send(JSON.stringify(e)), n.onload = function() {
                            300 <= n.status && console.warn("Non-2xx response received from server")
                        }
                    }
                }, {
                    key: "postYes",
                    value: function() {
                        this.token = x(), this.post("satisfied", {
                            isSatisfied: !0,
                            url: this.getUrl()
                        })
                    }
                }, {
                    key: "postNo",
                    value: function() {
                        this.token = x(), this.post("satisfied", {
                            isSatisfied: !1,
                            url: this.getUrl()
                        })
                    }
                }, {
                    key: "postComment",
                    value: function(e) {
                        this.post("comments", {
                            comments: e
                        })
                    }
                }]);
                var O = C;

                function C(e) {
                    P(this, C), this.endpoint = e, this.currentUrl = window.location.href, this.token = null
                }
                n(5);
                I(T, [{
                    key: "onYes",
                    value: function() {
                        this.isSatisfiedResponse = !0, this.postData.postYes(), new(!1 === this.enableTextResponse ? h : f)(this).render(), g(this.container, !0)
                    }
                }, {
                    key: "onNo",
                    value: function() {
                        this.isSatisfiedResponse = !1, this.postData.postNo(), new(!1 === this.enableTextResponse ? h : f)(this).render(), g(this.container, !1)
                    }
                }, {
                    key: "onTextSubmit",
                    value: function(e) {
                        this.postData.postComment(e), new h(this).render()
                    }
                }, {
                    key: "render",
                    value: function() {
                        new l(this).render()
                    }
                }]);
                var A = T;

                function T(e) {
                    var t;
                    if (P(this, T), this.container = document.querySelector(e.cssSelector), this.settings = j(j({}, {
                            enableTextResponse: (t = this.container).hasAttribute("data-enable-text-response"),
                            formEndpoint: t.getAttribute("data-form-endpoint")
                        }), e), !this.settings.formEndpoint) throw Error("formEndpoint setting or data-form-endpoint attribute must be defined");
                    this.postData = new O(this.settings.formEndpoint), this.isSatisfiedResponse = null, this.enableTextResponse = this.settings.enableTextResponse
                }
                t.default = function() {
                    var e = j({
                        cssSelector: "#nhsuk-user-feedback-form"
                    }, 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {});
                    new A(e).render()
                }
            }], r = {}, o.m = n, o.c = r, o.d = function(e, t, n) {
                o.o(e, t) || Object.defineProperty(e, t, {
                    enumerable: !0,
                    get: n
                })
            }, o.r = function(e) {
                "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                    value: "Module"
                }), Object.defineProperty(e, "__esModule", {
                    value: !0
                })
            }, o.t = function(t, e) {
                if (1 & e && (t = o(t)), 8 & e) return t;
                if (4 & e && "object" == a(t) && t && t.__esModule) return t;
                var n = Object.create(null);
                if (o.r(n), Object.defineProperty(n, "default", {
                        enumerable: !0,
                        value: t
                    }), 2 & e && "string" != typeof t)
                    for (var r in t) o.d(n, r, function(e) {
                        return t[e]
                    }.bind(null, r));
                return n
            }, o.n = function(e) {
                var t = e && e.__esModule ? function() {
                    return e.default
                } : function() {
                    return e
                };
                return o.d(t, "a", t), t
            }, o.o = function(e, t) {
                return Object.prototype.hasOwnProperty.call(e, t)
            }, o.p = "", o(o.s = 4);

            function o(e) {
                if (r[e]) return r[e].exports;
                var t = r[e] = {
                    i: e,
                    l: !1,
                    exports: {}
                };
                return n[e].call(t.exports, t, t.exports, o), t.l = !0, t.exports
            }
            var n, r
        }, "object" == a(s) && "object" == a(e) ? e.exports = t() : void 0 !== (t = "function" == typeof(t = t) ? t.apply(s, []) : t) && (e.exports = t)
    }.call(this, t(0)(e))
}, function(e, n, t) {
    ! function(e) {
        var t;

        function i(e) {
            return (i = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                return typeof e
            } : function(e) {
                return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
            })(e)
        }
        t = function() {
            return n = [function(e, n, t) {
                ! function(e) {
                    var t;

                    function g(e) {
                        return (g = "function" == typeof Symbol && "symbol" == i(Symbol.iterator) ? function(e) {
                            return i(e)
                        } : function(e) {
                            return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : i(e)
                        })(e)
                    }
                    window, t = function() {
                        return n = [function(e, t, n) {
                            function p(e, t, n) {
                                var r, o, i, a = e & p.F,
                                    s = e & p.G,
                                    u = e & p.P,
                                    c = e & p.B,
                                    l = s ? h : e & p.S ? h[t] || (h[t] = {}) : (h[t] || {})[g],
                                    d = s ? m : m[t] || (m[t] = {}),
                                    f = d[g] || (d[g] = {});
                                for (r in n = s ? t : n) o = ((i = !a && l && void 0 !== l[r]) ? l : n)[r], i = c && i ? y(o, h) : u && "function" == typeof o ? y(Function.call, o) : o, l && b(l, r, o, e & p.U), d[r] != o && v(d, r, i), u && f[r] != o && (f[r] = o)
                            }
                            var h = n(1),
                                m = n(6),
                                v = n(7),
                                b = n(16),
                                y = n(18),
                                g = "prototype";
                            h.core = m, p.F = 1, p.G = 2, p.S = 4, p.P = 8, p.B = 16, p.W = 32, p.U = 64, p.R = 128, e.exports = p
                        }, function(e, t) {
                            e = e.exports = "undefined" != typeof window && window.Math == Math ? window : "undefined" != typeof self && self.Math == Math ? self : Function("return this")();
                            "number" == typeof __g && (__g = e)
                        }, function(e, t) {
                            e.exports = function(e) {
                                return "object" == g(e) ? null !== e : "function" == typeof e
                            }
                        }, function(e, t, n) {
                            e.exports = !n(4)(function() {
                                return 7 != Object.defineProperty({}, "a", {
                                    get: function() {
                                        return 7
                                    }
                                }).a
                            })
                        }, function(e, t) {
                            e.exports = function(e) {
                                try {
                                    return !!e()
                                } catch (e) {
                                    return !0
                                }
                            }
                        }, function(y, e, t) {
                            "use strict";
                            t.r(e), t.d(e, "h", function() {
                                return n
                            }), t.d(e, "createElement", function() {
                                return n
                            }), t.d(e, "cloneElement", function() {
                                return o
                            }), t.d(e, "Component", function() {
                                return v
                            }), t.d(e, "render", function() {
                                return b
                            }), t.d(e, "rerender", function() {
                                return d
                            }), t.d(e, "options", function() {
                                return _
                            });
                            var u = function() {},
                                _ = {},
                                c = [],
                                l = [];

                            function n(e, t) {
                                for (var n, r, o, i = l, a = arguments.length; 2 < a--;) c.push(arguments[a]);
                                for (t && null != t.children && (c.length || c.push(t.children), delete t.children); c.length;)
                                    if ((r = c.pop()) && void 0 !== r.pop)
                                        for (a = r.length; a--;) c.push(r[a]);
                                    else "boolean" == typeof r && (r = null), (o = "function" != typeof e) && (null == r ? r = "" : "number" == typeof r ? r = String(r) : "string" != typeof r && (o = !1)), o && n ? i[i.length - 1] += r : i === l ? i = [r] : i.push(r), n = o;
                                var s = new u;
                                return s.nodeName = e, s.children = i, s.attributes = null == t ? void 0 : t, s.key = null == t ? void 0 : t.key, void 0 !== _.vnode && _.vnode(s), s
                            }

                            function k(e, t) {
                                for (var n in t) e[n] = t[n];
                                return e
                            }
                            var r = "function" == typeof Promise ? Promise.resolve().then.bind(Promise.resolve()) : setTimeout;

                            function o(e, t) {
                                return n(e.nodeName, k(k({}, e.attributes), t), 2 < arguments.length ? [].slice.call(arguments, 2) : e.children)
                            }
                            var s = /acit|ex(?:s|g|n|p|$)|rph|ows|mnc|ntw|ine[ch]|zoo|^ord/i,
                                i = [];

                            function a(e) {
                                !e._dirty && (e._dirty = !0) && 1 == i.push(e) && (_.debounceRendering || r)(d)
                            }

                            function d() {
                                var e, t = i;
                                for (i = []; e = t.pop();) e._dirty && O(e)
                            }

                            function Q(e, t) {
                                return e.normalizedNodeName === t || e.nodeName.toLowerCase() === t.toLowerCase()
                            }

                            function Y(e) {
                                var t = k({}, e.attributes),
                                    n = (t.children = e.children, e.nodeName.defaultProps);
                                if (void 0 !== n)
                                    for (var r in n) void 0 === t[r] && (t[r] = n[r]);
                                return t
                            }

                            function J(e) {
                                var t = e.parentNode;
                                t && t.removeChild(e)
                            }

                            function X(e, t, n, r, o) {
                                if ("key" !== (t = "className" === t ? "class" : t))
                                    if ("ref" === t) n && n(null), r && r(e);
                                    else if ("class" !== t || o)
                                    if ("style" === t) {
                                        if (r && "string" != typeof r && "string" != typeof n || (e.style.cssText = r || ""), r && "object" == g(r)) {
                                            if ("string" != typeof n)
                                                for (var i in n) i in r || (e.style[i] = "");
                                            for (var i in r) e.style[i] = "number" == typeof r[i] && !1 === s.test(i) ? r[i] + "px" : r[i]
                                        }
                                    } else if ("dangerouslySetInnerHTML" === t) r && (e.innerHTML = r.__html || "");
                                else if ("o" == t[0] && "n" == t[1]) {
                                    var a = t !== (t = t.replace(/Capture$/, ""));
                                    t = t.toLowerCase().substring(2), r ? n || e.addEventListener(t, f, a) : e.removeEventListener(t, f, a), (e._listeners || (e._listeners = {}))[t] = r
                                } else if ("list" !== t && "type" !== t && !o && t in e) {
                                    try {
                                        e[t] = null == r ? "" : r
                                    } catch (e) {}
                                    null != r && !1 !== r || "spellcheck" == t || e.removeAttribute(t)
                                } else {
                                    n = o && t !== (t = t.replace(/^xlink:?/, ""));
                                    null == r || !1 === r ? n ? e.removeAttributeNS("http://www.w3.org/1999/xlink", t.toLowerCase()) : e.removeAttribute(t) : "function" != typeof r && (n ? e.setAttributeNS("http://www.w3.org/1999/xlink", t.toLowerCase(), r) : e.setAttribute(t, r))
                                } else e.className = r || ""
                            }

                            function f(e) {
                                return this._listeners[e.type](_.event && _.event(e) || e)
                            }
                            var S = [],
                                E = 0,
                                Z = !1,
                                ee = !1;

                            function x() {
                                for (var e; e = S.pop();) _.afterMount && _.afterMount(e), e.componentDidMount && e.componentDidMount()
                            }

                            function te(e, t, R, q, n) {
                                var r = e,
                                    B = Z;
                                if ("string" == typeof(t = null != t && "boolean" != typeof t ? t : "") || "number" == typeof t) e && void 0 !== e.splitText && e.parentNode && (!e._component || n) ? e.nodeValue != t && (e.nodeValue = t) : (r = document.createTextNode(t), e && (e.parentNode && e.parentNode.replaceChild(r, e), ne(e, !0))), r.__preactattr_ = !0;
                                else {
                                    n = t.nodeName;
                                    if ("function" == typeof n) {
                                        var o = e;
                                        var i = t;
                                        var a = R;
                                        var s = q;
                                        for (var u = o && o._component, c = u, l = o, d = u && o._componentConstructor === i.nodeName, f = d, p = Y(i); u && !f && (u = u._parentComponent);) f = u.constructor === i.nodeName;
                                        return u && f && (!s || u._component) ? (oe(u, p, 3, a, s), o = u.base) : (c && !d && (ie(c), o = l = null), u = re(i.nodeName, p, a), o && !u.nextBase && (u.nextBase = o, l = null), oe(u, p, 1, a, s), o = u.base, l && o !== l && (l._component = null, ne(l, !1))), o;
                                        return
                                    }
                                    if (Z = "svg" === n || "foreignObject" !== n && Z, n = String(n), (!e || !Q(e, n)) && (d = n, (c = Z ? document.createElementNS("http://www.w3.org/2000/svg", d) : document.createElement(d)).normalizedNodeName = d, r = c, e)) {
                                        for (; e.firstChild;) r.appendChild(e.firstChild);
                                        e.parentNode && e.parentNode.replaceChild(r, e), ne(e, !0)
                                    }
                                    var p = r.firstChild,
                                        h = r.__preactattr_,
                                        a = t.children;
                                    if (null == h)
                                        for (var h = r.__preactattr_ = {}, m = r.attributes, v = m.length; v--;) h[m[v].name] = m[v].value;
                                    if (!ee && a && 1 === a.length && "string" == typeof a[0] && null != p && void 0 !== p.splitText && null == p.nextSibling) p.nodeValue != a[0] && (p.nodeValue = a[0]);
                                    else if (a && a.length || null != p) {
                                        var b = r;
                                        var y = a;
                                        var D = R;
                                        var H = q;
                                        var g = ee || null != h.dangerouslySetInnerHTML;
                                        var w, U, _, F, k, S, V, K = b.childNodes,
                                            E = [],
                                            x = {},
                                            O = 0,
                                            C = 0,
                                            W = K.length,
                                            A = 0,
                                            $ = y ? y.length : 0;
                                        if (0 !== W)
                                            for (var T = 0; T < W; T++) {
                                                var j = K[T],
                                                    G = j.__preactattr_;
                                                null != (L = $ && G ? j._component ? j._component.__key : G.key : null) ? (O++, x[L] = j) : (G || (void 0 !== j.splitText ? !g || j.nodeValue.trim() : g)) && (E[A++] = j)
                                            }
                                        if (0 !== $)
                                            for (T = 0; T < $; T++) {
                                                var L, N = null;
                                                if (null != (L = (F = y[T]).key)) O && void 0 !== x[L] && (N = x[L], x[L] = void 0, O--);
                                                else if (C < A)
                                                    for (w = C; w < A; w++)
                                                        if (void 0 !== E[w] && (k = U = E[w], V = g, "string" == typeof(S = F) || "number" == typeof S ? void 0 !== k.splitText : "string" == typeof S.nodeName ? !k._componentConstructor && Q(k, S.nodeName) : V || k._componentConstructor === S.nodeName)) {
                                                            N = U, E[w] = void 0, w === A - 1 && A--, w === C && C++;
                                                            break
                                                        }
                                                N = te(N, F, D, H), _ = K[T], N && N !== b && N !== _ && (null == _ ? b.appendChild(N) : N === _.nextSibling ? J(_) : b.insertBefore(N, _))
                                            }
                                        if (O)
                                            for (var T in x) void 0 !== x[T] && ne(x[T], !1);
                                        for (; C <= A;) void 0 !== (N = E[A--]) && ne(N, !1)
                                    }
                                    var P, z = r,
                                        I = t.attributes,
                                        M = h;
                                    for (P in M) I && null != I[P] || null == M[P] || X(z, P, M[P], M[P] = void 0, Z);
                                    for (P in I) "children" === P || "innerHTML" === P || P in M && I[P] === ("value" === P || "checked" === P ? z : M)[P] || X(z, P, M[P], M[P] = I[P], Z);
                                    Z = B
                                }
                                return r
                            }

                            function ne(e, t) {
                                var n = e._component;
                                n ? ie(n) : (null != e.__preactattr_ && e.__preactattr_.ref && e.__preactattr_.ref(null), !1 !== t && null != e.__preactattr_ || J(e), p(e))
                            }

                            function p(e) {
                                for (e = e.lastChild; e;) {
                                    var t = e.previousSibling;
                                    ne(e, !0), e = t
                                }
                            }
                            var h = [];

                            function re(e, t, n) {
                                var r, o = h.length;
                                for (e.prototype && e.prototype.render ? (r = new e(t, n), v.call(r, t, n)) : ((r = new v(t, n)).constructor = e, r.render = m); o--;)
                                    if (h[o].constructor === e) return r.nextBase = h[o].nextBase, h.splice(o, 1), r;
                                return r
                            }

                            function m(e, t, n) {
                                return this.constructor(e, n)
                            }

                            function oe(e, t, n, r, o) {
                                e._disable || (e._disable = !0, e.__ref = t.ref, e.__key = t.key, delete t.ref, delete t.key, void 0 === e.constructor.getDerivedStateFromProps && (!e.base || o ? e.componentWillMount && e.componentWillMount() : e.componentWillReceiveProps && e.componentWillReceiveProps(t, r)), r && r !== e.context && (e.prevContext || (e.prevContext = e.context), e.context = r), e.prevProps || (e.prevProps = e.props), e.props = t, e._disable = !1, 0 !== n && (1 !== n && !1 === _.syncComponentUpdates && e.base ? a(e) : O(e, 1, o)), e.__ref && e.__ref(e))
                            }

                            function O(e, t, n, r) {
                                if (!e._disable) {
                                    var o, i = e.props,
                                        a = e.state,
                                        s = e.context,
                                        u = e.prevProps || i,
                                        c = e.prevState || a,
                                        l = e.prevContext || s,
                                        d = e.base,
                                        f = e.nextBase,
                                        p = d || f,
                                        h = e._component,
                                        m = !1,
                                        v = l;
                                    if (e.constructor.getDerivedStateFromProps && (a = k(k({}, a), e.constructor.getDerivedStateFromProps(i, a)), e.state = a), d && (e.props = u, e.state = c, e.context = l, 2 !== t && e.shouldComponentUpdate && !1 === e.shouldComponentUpdate(i, a, s) ? m = !0 : e.componentWillUpdate && e.componentWillUpdate(i, a, s), e.props = i, e.state = a, e.context = s), e.prevProps = e.prevState = e.prevContext = e.nextBase = null, e._dirty = !1, !m) {
                                        l = e.render(i, a, s), e.getChildContext && (s = k(k({}, s), e.getChildContext())), d && e.getSnapshotBeforeUpdate && (v = e.getSnapshotBeforeUpdate(u, c));
                                        var b, y, i = l && l.nodeName;
                                        if ("function" == typeof i ? (a = Y(l), (o = h) && o.constructor === i && a.key == o.__key ? oe(o, a, 1, s, !1) : (b = o, e._component = o = re(i, a, s), o.nextBase = o.nextBase || f, o._parentComponent = e, oe(o, a, 0, s, !1), O(o, 1, n, !0)), y = o.base) : (i = p, (b = h) && (i = e._component = null), !p && 1 !== t || (i && (i._component = null), y = function(e, t, n, r, o) {
                                                E++ || (Z = null != o && void 0 !== o.ownerSVGElement, ee = null != e && !("__preactattr_" in e));
                                                e = te(e, t, n, r, !0);
                                                return o && e.parentNode !== o && o.appendChild(e), --E || (ee = !1), e
                                            }(i, l, s, n || !d, p && p.parentNode))), !p || y === p || o === h || (f = p.parentNode) && y !== f && (f.replaceChild(y, p), b || (p._component = null, ne(p, !1))), b && ie(b), (e.base = y) && !r) {
                                            for (var g = e, w = e; w = w._parentComponent;)(g = w).base = y;
                                            y._component = g, y._componentConstructor = g.constructor
                                        }
                                    }
                                    for (!d || n ? S.unshift(e) : m || (e.componentDidUpdate && e.componentDidUpdate(u, c, v), _.afterUpdate && _.afterUpdate(e)); e._renderCallbacks.length;) e._renderCallbacks.pop().call(e);
                                    E || r || x()
                                }
                            }

                            function ie(e) {
                                _.beforeUnmount && _.beforeUnmount(e);
                                var t = e.base,
                                    n = (e._disable = !0, e.componentWillUnmount && e.componentWillUnmount(), e.base = null, e._component);
                                n ? ie(n) : t && (t.__preactattr_ && t.__preactattr_.ref && t.__preactattr_.ref(null), J(e.nextBase = t), h.push(e), p(t)), e.__ref && e.__ref(null)
                            }

                            function v(e, t) {
                                this._dirty = !0, this.context = t, this.props = e, this.state = this.state || {}, this._renderCallbacks = []
                            }

                            function b(e, t, n) {
                                return E++ || (Z = null != t && void 0 !== t.ownerSVGElement, ee = null != n && !("__preactattr_" in n)), n = te(n, e, {}, !1, !1), t && n.parentNode !== t && t.appendChild(n), --E || (ee = !1, x()), n
                            }
                            k(v.prototype, {
                                setState: function(e, t) {
                                    this.prevState || (this.prevState = this.state), this.state = k(k({}, this.state), "function" == typeof e ? e(this.state, this.props) : e), t && this._renderCallbacks.push(t), a(this)
                                },
                                forceUpdate: function(e) {
                                    e && this._renderCallbacks.push(e), O(this, 2)
                                },
                                render: function() {}
                            }), e.default = {
                                h: n,
                                createElement: n,
                                cloneElement: o,
                                Component: v,
                                render: b,
                                rerender: d,
                                options: _
                            }
                        }, function(e, t) {
                            e = e.exports = {
                                version: "2.5.7"
                            };
                            "number" == typeof __e && (__e = e)
                        }, function(e, t, n) {
                            var r = n(8),
                                o = n(40);
                            e.exports = n(3) ? function(e, t, n) {
                                return r.f(e, t, o(1, n))
                            } : function(e, t, n) {
                                return e[t] = n, e
                            }
                        }, function(e, t, n) {
                            var r = n(9),
                                o = n(38),
                                i = n(39),
                                a = Object.defineProperty;
                            t.f = n(3) ? Object.defineProperty : function(e, t, n) {
                                if (r(e), t = i(t, !0), r(n), o) try {
                                    return a(e, t, n)
                                } catch (e) {}
                                if ("get" in n || "set" in n) throw TypeError("Accessors not supported!");
                                return "value" in n && (e[t] = n.value), e
                            }
                        }, function(e, t, n) {
                            var r = n(2);
                            e.exports = function(e) {
                                if (r(e)) return e;
                                throw TypeError(e + " is not an object!")
                            }
                        }, function(e, t) {
                            var n = 0,
                                r = Math.random();
                            e.exports = function(e) {
                                return "Symbol(".concat(void 0 === e ? "" : e, ")_", (++n + r).toString(36))
                            }
                        }, function(e, t, n) {
                            var r = n(22);
                            e.exports = Object("z").propertyIsEnumerable(0) ? Object : function(e) {
                                return "String" == r(e) ? e.split("") : Object(e)
                            }
                        }, function(e, t) {
                            e.exports = function(e) {
                                if (null == e) throw TypeError("Can't call method on  " + e);
                                return e
                            }
                        }, function(e, t, n) {
                            "use strict";
                            var r = n(4);
                            e.exports = function(e, t) {
                                return !!e && r(function() {
                                    t ? e.call(null, function() {}, 1) : e.call(null)
                                })
                            }
                        }, function(e, t, n) {
                            var r = n(0);
                            r(r.S + r.F, "Object", {
                                assign: n(41)
                            })
                        }, function(e, t, n) {
                            var r = n(2),
                                o = n(1).document,
                                i = r(o) && r(o.createElement);
                            e.exports = function(e) {
                                return i ? o.createElement(e) : {}
                            }
                        }, function(e, t, n) {
                            var i = n(1),
                                a = n(7),
                                s = n(17),
                                u = n(10)("src"),
                                r = "toString",
                                o = Function[r],
                                c = ("" + o).split(r);
                            n(6).inspectSource = function(e) {
                                return o.call(e)
                            }, (e.exports = function(e, t, n, r) {
                                var o = "function" == typeof n;
                                o && !s(n, "name") && a(n, "name", t), e[t] !== n && (o && !s(n, u) && a(n, u, e[t] ? "" + e[t] : c.join(String(t))), e === i ? e[t] = n : r ? e[t] ? e[t] = n : a(e, t, n) : (delete e[t], a(e, t, n)))
                            })(Function.prototype, r, function() {
                                return "function" == typeof this && this[u] || o.call(this)
                            })
                        }, function(e, t) {
                            var n = {}.hasOwnProperty;
                            e.exports = function(e, t) {
                                return n.call(e, t)
                            }
                        }, function(e, t, n) {
                            var i = n(19);
                            e.exports = function(r, o, e) {
                                if (i(r), void 0 === o) return r;
                                switch (e) {
                                    case 1:
                                        return function(e) {
                                            return r.call(o, e)
                                        };
                                    case 2:
                                        return function(e, t) {
                                            return r.call(o, e, t)
                                        };
                                    case 3:
                                        return function(e, t, n) {
                                            return r.call(o, e, t, n)
                                        }
                                }
                                return function() {
                                    return r.apply(o, arguments)
                                }
                            }
                        }, function(e, t) {
                            e.exports = function(e) {
                                if ("function" != typeof e) throw TypeError(e + " is not a function!");
                                return e
                            }
                        }, function(e, t, n) {
                            var r = n(42),
                                o = n(28);
                            e.exports = Object.keys || function(e) {
                                return r(e, o)
                            }
                        }, function(e, t, n) {
                            var r = n(11),
                                o = n(12);
                            e.exports = function(e) {
                                return r(o(e))
                            }
                        }, function(e, t) {
                            var n = {}.toString;
                            e.exports = function(e) {
                                return n.call(e).slice(8, -1)
                            }
                        }, function(e, t, n) {
                            var u = n(21),
                                c = n(24),
                                l = n(43);
                            e.exports = function(s) {
                                return function(e, t, n) {
                                    var r, o = u(e),
                                        i = c(o.length),
                                        a = l(n, i);
                                    if (s && t != t) {
                                        for (; a < i;)
                                            if ((r = o[a++]) != r) return !0
                                    } else
                                        for (; a < i; a++)
                                            if ((s || a in o) && o[a] === t) return s || a || 0;
                                    return !s && -1
                                }
                            }
                        }, function(e, t, n) {
                            var r = n(25),
                                o = Math.min;
                            e.exports = function(e) {
                                return 0 < e ? o(r(e), 9007199254740991) : 0
                            }
                        }, function(e, t) {
                            var n = Math.ceil,
                                r = Math.floor;
                            e.exports = function(e) {
                                return isNaN(e = +e) ? 0 : (0 < e ? r : n)(e)
                            }
                        }, function(e, t, n) {
                            var r = n(27)("keys"),
                                o = n(10);
                            e.exports = function(e) {
                                return r[e] || (r[e] = o(e))
                            }
                        }, function(e, t, n) {
                            var r = n(6),
                                o = n(1),
                                i = "__core-js_shared__",
                                a = o[i] || (o[i] = {});
                            (e.exports = function(e, t) {
                                return a[e] || (a[e] = void 0 !== t ? t : {})
                            })("versions", []).push({
                                version: r.version,
                                mode: n(44) ? "pure" : "global",
                                copyright: "© 2018 Denis Pushkarev (zloirock.ru)"
                            })
                        }, function(e, t) {
                            e.exports = "constructor,hasOwnProperty,isPrototypeOf,propertyIsEnumerable,toLocaleString,toString,valueOf".split(",")
                        }, function(e, t, n) {
                            var r = n(12);
                            e.exports = function(e) {
                                return Object(r(e))
                            }
                        }, function(e, t, n) {
                            var r = n(8).f,
                                o = Function.prototype,
                                i = /^\s*function ([^ (]*)/;
                            "name" in o || n(3) && r(o, "name", {
                                configurable: !0,
                                get: function() {
                                    try {
                                        return ("" + this).match(i)[1]
                                    } catch (e) {
                                        return ""
                                    }
                                }
                            })
                        }, function(e, t, n) {
                            "use strict";
                            var r = n(0),
                                o = n(32)(1);
                            r(r.P + r.F * !n(13)([].map, !0), "Array", {
                                map: function(e) {
                                    return o(this, e, arguments[1])
                                }
                            })
                        }, function(e, t, n) {
                            var g = n(18),
                                w = n(11),
                                _ = n(29),
                                k = n(24),
                                r = n(47);
                            e.exports = function(d, e) {
                                var f = 1 == d,
                                    p = 2 == d,
                                    h = 3 == d,
                                    m = 4 == d,
                                    v = 6 == d,
                                    b = 5 == d || v,
                                    y = e || r;
                                return function(e, t, n) {
                                    for (var r, o, i = _(e), a = w(i), s = g(t, n, 3), u = k(a.length), c = 0, l = f ? y(e, u) : p ? y(e, 0) : void 0; c < u; c++)
                                        if ((b || c in a) && (o = s(r = a[c], c, i), d))
                                            if (f) l[c] = o;
                                            else if (o) switch (d) {
                                        case 3:
                                            return !0;
                                        case 5:
                                            return r;
                                        case 6:
                                            return c;
                                        case 2:
                                            l.push(r)
                                    } else if (m) return !1;
                                    return v ? -1 : h || m ? m : l
                                }
                            }
                        }, function(e, t, n) {
                            var r = n(22);
                            e.exports = Array.isArray || function(e) {
                                return "Array" == r(e)
                            }
                        }, function(e, t, n) {
                            var r = n(27)("wks"),
                                o = n(10),
                                i = n(1).Symbol,
                                a = "function" == typeof i;
                            (e.exports = function(e) {
                                return r[e] || (r[e] = a && i[e] || (a ? i : o)("Symbol." + e))
                            }).store = r
                        }, function(e, t, n) {
                            "use strict";
                            var r = n(0),
                                o = n(23)(!1),
                                i = [].indexOf,
                                a = !!i && 1 / [1].indexOf(1, -0) < 0;
                            r(r.P + r.F * (a || !n(13)(i)), "Array", {
                                indexOf: function(e) {
                                    return a ? i.apply(this, arguments) || 0 : o(this, e, arguments[1])
                                }
                            })
                        }, function(e, t, n) {
                            var r = n(0);
                            r(r.S, "Object", {
                                create: n(52)
                            })
                        }, function(e, t, n) {
                            "use strict";
                            t.__esModule = !0, t.default = void 0, n(14), n(30), n(31), n(35), n(49), n(50);
                            var r = n(5),
                                o = (n = n(51)) && n.__esModule ? n : {
                                    default: n
                                };

                            function i(e) {
                                if (!e.element) throw new Error("element is not defined");
                                if (!e.id) throw new Error("id is not defined");
                                if (!e.source) throw new Error("source is not defined");
                                Array.isArray(e.source) && (e.source = a(e.source)), (0, r.render)((0, r.createElement)(o.default, e), e.element)
                            }
                            var a = function(n) {
                                return function(t, e) {
                                    e(n.filter(function(e) {
                                        return -1 !== e.toLowerCase().indexOf(t.toLowerCase())
                                    }))
                                }
                            };
                            i.enhanceSelectElement = function(n) {
                                if (!n.selectElement) throw new Error("selectElement is not defined");
                                n.source || (e = [].filter.call(n.selectElement.options, function(e) {
                                    return e.value || n.preserveNullOptions
                                }), n.source = e.map(function(e) {
                                    return e.textContent || e.innerText
                                })), n.onConfirm = n.onConfirm || function(t) {
                                    var e = [].filter.call(n.selectElement.options, function(e) {
                                        return (e.textContent || e.innerText) === t
                                    })[0];
                                    e && (e.selected = !0)
                                }, !n.selectElement.value && void 0 !== n.defaultValue || (e = n.selectElement.options[n.selectElement.options.selectedIndex], n.defaultValue = e.textContent || e.innerText), void 0 === n.name && (n.name = ""), void 0 === n.id && (void 0 === n.selectElement.id ? n.id = "" : n.id = n.selectElement.id), void 0 === n.autoselect && (n.autoselect = !0);
                                var e = document.createElement("div");
                                n.selectElement.parentNode.insertBefore(e, n.selectElement), i(Object.assign({}, n, {
                                    element: e
                                })), n.selectElement.style.display = "none", n.selectElement.id = n.selectElement.id + "-select"
                            }, t.default = i
                        }, function(e, t, n) {
                            e.exports = !n(3) && !n(4)(function() {
                                return 7 != Object.defineProperty(n(15)("div"), "a", {
                                    get: function() {
                                        return 7
                                    }
                                }).a
                            })
                        }, function(e, t, n) {
                            var o = n(2);
                            e.exports = function(e, t) {
                                if (!o(e)) return e;
                                var n, r;
                                if (t && "function" == typeof(n = e.toString) && !o(r = n.call(e)) || "function" == typeof(n = e.valueOf) && !o(r = n.call(e)) || !t && "function" == typeof(n = e.toString) && !o(r = n.call(e))) return r;
                                throw TypeError("Can't convert object to primitive value")
                            }
                        }, function(e, t) {
                            e.exports = function(e, t) {
                                return {
                                    enumerable: !(1 & e),
                                    configurable: !(2 & e),
                                    writable: !(4 & e),
                                    value: t
                                }
                            }
                        }, function(e, t, n) {
                            "use strict";
                            var f = n(20),
                                p = n(45),
                                h = n(46),
                                m = n(29),
                                v = n(11),
                                o = Object.assign;
                            e.exports = !o || n(4)(function() {
                                var e = {},
                                    t = {},
                                    n = Symbol(),
                                    r = "abcdefghijklmnopqrst";
                                return e[n] = 7, r.split("").forEach(function(e) {
                                    t[e] = e
                                }), 7 != o({}, e)[n] || Object.keys(o({}, t)).join("") != r
                            }) ? function(e, t) {
                                for (var n = m(e), r = arguments.length, o = 1, i = p.f, a = h.f; o < r;)
                                    for (var s, u = v(arguments[o++]), c = i ? f(u).concat(i(u)) : f(u), l = c.length, d = 0; d < l;) a.call(u, s = c[d++]) && (n[s] = u[s]);
                                return n
                            } : o
                        }, function(e, t, n) {
                            var a = n(17),
                                s = n(21),
                                u = n(23)(!1),
                                c = n(26)("IE_PROTO");
                            e.exports = function(e, t) {
                                var n, r = s(e),
                                    o = 0,
                                    i = [];
                                for (n in r) n != c && a(r, n) && i.push(n);
                                for (; t.length > o;) !a(r, n = t[o++]) || ~u(i, n) || i.push(n);
                                return i
                            }
                        }, function(e, t, n) {
                            var r = n(25),
                                o = Math.max,
                                i = Math.min;
                            e.exports = function(e, t) {
                                return (e = r(e)) < 0 ? o(e + t, 0) : i(e, t)
                            }
                        }, function(e, t) {
                            e.exports = !1
                        }, function(e, t) {
                            t.f = Object.getOwnPropertySymbols
                        }, function(e, t) {
                            t.f = {}.propertyIsEnumerable
                        }, function(e, t, n) {
                            var r = n(48);
                            e.exports = function(e, t) {
                                return new(r(e))(t)
                            }
                        }, function(e, t, n) {
                            var r = n(2),
                                o = n(33),
                                i = n(34)("species");
                            e.exports = function(e) {
                                var t;
                                return o(e) && ("function" != typeof(t = e.constructor) || t !== Array && !o(t.prototype) || (t = void 0), r(t) && null === (t = t[i]) && (t = void 0)), void 0 === t ? Array : t
                            }
                        }, function(e, t, n) {
                            "use strict";
                            var r = n(0),
                                o = n(32)(2);
                            r(r.P + r.F * !n(13)([].filter, !0), "Array", {
                                filter: function(e) {
                                    return o(this, e, arguments[1])
                                }
                            })
                        }, function(e, t, n) {
                            var r = n(0);
                            r(r.S, "Array", {
                                isArray: n(33)
                            })
                        }, function(e, t, n) {
                            "use strict";
                            t.__esModule = !0, t.default = void 0, n(14), n(36), n(30), n(31), n(35), n(55), n(58);
                            var B = n(5),
                                D = r(n(60)),
                                n = r(n(61));

                            function r(e) {
                                return e && e.__esModule ? e : {
                                    default: e
                                }
                            }

                            function H() {
                                return (H = Object.assign || function(e) {
                                    for (var t = 1; t < arguments.length; t++) {
                                        var n, r = arguments[t];
                                        for (n in r) Object.prototype.hasOwnProperty.call(r, n) && (e[n] = r[n])
                                    }
                                    return e
                                }).apply(this, arguments)
                            }

                            function o(e) {
                                if (void 0 === e) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
                                return e
                            }
                            var i = {
                                13: "enter",
                                27: "escape",
                                32: "space",
                                38: "up",
                                40: "down"
                            };

                            function U() {
                                return "undefined" != typeof navigator && !(!navigator.userAgent.match(/(iPod|iPhone|iPad)/g) || !navigator.userAgent.match(/AppleWebKit/g))
                            }
                            a = B.Component, u = a, (s = c).prototype = Object.create(u.prototype), (s.prototype.constructor = s).__proto__ = u, (s = c.prototype).isQueryAnOption = function(e, t) {
                                var n = this;
                                return -1 !== t.map(function(e) {
                                    return n.templateInputValue(e).toLowerCase()
                                }).indexOf(e.toLowerCase())
                            }, s.componentDidMount = function() {
                                this.pollInputElement()
                            }, s.componentWillUnmount = function() {
                                clearTimeout(this.$pollInput)
                            }, s.pollInputElement = function() {
                                var e = this;
                                this.getDirectInputChanges(), this.$pollInput = setTimeout(function() {
                                    e.pollInputElement()
                                }, 100)
                            }, s.getDirectInputChanges = function() {
                                var e = this.elementReferences[-1];
                                e && e.value !== this.state.query && this.handleInputChange({
                                    target: {
                                        value: e.value
                                    }
                                })
                            }, s.componentDidUpdate = function(e, t) {
                                var n = this.state.focused,
                                    r = t.focused !== n;
                                !r || null === n || this.elementReferences[n].focus();
                                r = r && null === t.focused; - 1 === n && r && (t = this.elementReferences[n]).setSelectionRange(0, t.value.length)
                            }, s.hasAutoselect = function() {
                                return !U() && this.props.autoselect
                            }, s.templateInputValue = function(e) {
                                var t = this.props.templates && this.props.templates.inputValue;
                                return t ? t(e) : e
                            }, s.templateSuggestion = function(e) {
                                var t = this.props.templates && this.props.templates.suggestion;
                                return t ? t(e) : e
                            }, s.handleComponentBlur = function(e) {
                                var t, n = this.state,
                                    r = n.options,
                                    o = n.query,
                                    n = n.selected;
                                this.props.confirmOnBlur ? (t = e.query || o, this.props.onConfirm(r[n])) : t = o, this.setState({
                                    focused: null,
                                    menuOpen: e.menuOpen || !1,
                                    query: t,
                                    selected: null,
                                    validChoiceMade: this.isQueryAnOption(t, r)
                                })
                            }, s.handleListMouseLeave = function(e) {
                                this.setState({
                                    hovered: null
                                })
                            }, s.handleOptionBlur = function(e, t) {
                                var n = this.state,
                                    r = n.focused,
                                    o = n.menuOpen,
                                    i = n.options,
                                    n = n.selected,
                                    a = null === e.relatedTarget,
                                    e = e.relatedTarget === this.elementReferences[-1],
                                    t = r !== t && -1 !== r;
                                (!t && a || !t && !e) && (r = o && U(), this.handleComponentBlur({
                                    menuOpen: r,
                                    query: this.templateInputValue(i[n])
                                }))
                            }, s.handleInputBlur = function(e) {
                                var t = this.state,
                                    n = t.focused,
                                    r = t.menuOpen,
                                    o = t.options,
                                    i = t.query,
                                    t = t.selected; - 1 === n && (n = r && U(), r = U() ? i : this.templateInputValue(o[t]), this.handleComponentBlur({
                                    menuOpen: n,
                                    query: r
                                }))
                            }, s.handleInputChange = function(e) {
                                var n = this,
                                    t = this.props,
                                    r = t.minLength,
                                    o = t.source,
                                    t = t.showAllValues,
                                    i = this.hasAutoselect(),
                                    e = e.target.value,
                                    a = 0 === e.length,
                                    s = this.state.query.length !== e.length,
                                    r = e.length >= r;
                                this.setState({
                                    query: e,
                                    ariaHint: a
                                }), t || !a && s && r ? o(e, function(e) {
                                    var t = 0 < e.length;
                                    n.setState({
                                        menuOpen: t,
                                        options: e,
                                        selected: i && t ? 0 : -1,
                                        validChoiceMade: !1
                                    })
                                }) : !a && r || this.setState({
                                    menuOpen: !1,
                                    options: []
                                })
                            }, s.handleInputClick = function(e) {
                                this.handleInputChange(e)
                            }, s.handleInputFocus = function(e) {
                                var t = this.state,
                                    n = t.query,
                                    r = t.validChoiceMade,
                                    t = t.options,
                                    o = this.props.minLength,
                                    i = !r && n.length >= o && 0 < t.length;
                                i ? this.setState(function(e) {
                                    e = e.menuOpen;
                                    return {
                                        focused: -1,
                                        menuOpen: i || e,
                                        selected: -1
                                    }
                                }) : this.setState({
                                    focused: -1
                                })
                            }, s.handleOptionFocus = function(e) {
                                this.setState({
                                    focused: e,
                                    hovered: null,
                                    selected: e
                                })
                            }, s.handleOptionMouseEnter = function(e, t) {
                                U() || this.setState({
                                    hovered: t
                                })
                            }, s.handleOptionClick = function(e, t) {
                                var t = this.state.options[t],
                                    n = this.templateInputValue(t);
                                this.props.onConfirm(t), this.setState({
                                    focused: -1,
                                    hovered: null,
                                    menuOpen: !1,
                                    query: n,
                                    selected: -1,
                                    validChoiceMade: !0
                                }), this.forceUpdate()
                            }, s.handleOptionMouseDown = function(e) {
                                e.preventDefault()
                            }, s.handleUpArrow = function(e) {
                                e.preventDefault();
                                var e = this.state,
                                    t = e.menuOpen,
                                    e = e.selected; - 1 !== e && t && this.handleOptionFocus(e - 1)
                            }, s.handleDownArrow = function(e) {
                                var t, n, r = this;
                                e.preventDefault(), this.props.showAllValues && !1 === this.state.menuOpen ? (e.preventDefault(), this.props.source("", function(e) {
                                    r.setState({
                                        menuOpen: !0,
                                        options: e,
                                        selected: 0,
                                        focused: 0,
                                        hovered: null
                                    })
                                })) : !0 === this.state.menuOpen && (t = (e = this.state).menuOpen, n = e.options, (e = e.selected) !== n.length - 1 && t && this.handleOptionFocus(e + 1))
                            }, s.handleSpace = function(e) {
                                var t = this;
                                this.props.showAllValues && !1 === this.state.menuOpen && "" === this.state.query && (e.preventDefault(), this.props.source("", function(e) {
                                    t.setState({
                                        menuOpen: !0,
                                        options: e
                                    })
                                })), -1 !== this.state.focused && (e.preventDefault(), this.handleOptionClick(e, this.state.focused))
                            }, s.handleEnter = function(e) {
                                this.state.menuOpen && (e.preventDefault(), 0 <= this.state.selected && this.handleOptionClick(e, this.state.selected))
                            }, s.handlePrintableKey = function(e) {
                                var t = this.elementReferences[-1];
                                e.target !== t && t.focus()
                            }, s.handleKeyDown = function(e) {
                                switch (i[e.keyCode]) {
                                    case "up":
                                        this.handleUpArrow(e);
                                        break;
                                    case "down":
                                        this.handleDownArrow(e);
                                        break;
                                    case "space":
                                        this.handleSpace(e);
                                        break;
                                    case "enter":
                                        this.handleEnter(e);
                                        break;
                                    case "escape":
                                        this.handleComponentBlur({
                                            query: this.state.query
                                        });
                                        break;
                                    default:
                                        (47 < (t = e.keyCode) && t < 58 || 32 === t || 8 === t || 64 < t && t < 91 || 95 < t && t < 112 || 185 < t && t < 193 || 218 < t && t < 223) && this.handlePrintableKey(e)
                                }
                                var t
                            }, s.render = function() {
                                var e, i = this,
                                    t = this.props,
                                    n = t.cssNamespace,
                                    r = t.displayMenu,
                                    a = t.id,
                                    o = t.minLength,
                                    s = t.name,
                                    u = t.placeholder,
                                    c = t.required,
                                    l = t.showAllValues,
                                    d = t.tNoResults,
                                    f = t.tStatusQueryTooShort,
                                    p = t.tStatusNoResults,
                                    h = t.tStatusSelectedOption,
                                    m = t.tStatusResults,
                                    v = t.tAssistiveHint,
                                    t = t.dropdownArrow,
                                    b = this.state,
                                    y = b.focused,
                                    g = b.hovered,
                                    w = b.menuOpen,
                                    _ = b.options,
                                    k = b.query,
                                    S = b.selected,
                                    E = b.ariaHint,
                                    b = b.validChoiceMade,
                                    x = this.hasAutoselect(),
                                    O = 0 === _.length,
                                    C = 0 !== k.length,
                                    A = k.length >= o,
                                    O = this.props.showNoOptionsFound && -1 === y && O && C && A,
                                    C = n + "__wrapper",
                                    A = n + "__input",
                                    T = null !== y ? " " + A + "--focused" : "",
                                    j = this.props.showAllValues ? " " + A + "--show-all-values" : " " + A + "--default",
                                    L = n + "__dropdown-arrow-down",
                                    N = -1 !== y && null !== y,
                                    P = n + "__menu",
                                    r = P + "--" + r,
                                    R = P + "--" + (w || O ? "visible" : "hidden"),
                                    I = n + "__option",
                                    q = n + "__hint",
                                    M = this.templateInputValue(_[S]),
                                    x = M && 0 === M.toLowerCase().indexOf(k.toLowerCase()) && x ? k + M.substr(k.length) : "",
                                    M = a + "__assistiveHint",
                                    E = E ? {
                                        "aria-describedby": M
                                    } : null;
                                return l && "string" == typeof(e = t({
                                    className: L
                                })) && (e = (0, B.createElement)("div", {
                                    className: n + "__dropdown-arrow-down-wrapper",
                                    dangerouslySetInnerHTML: {
                                        __html: e
                                    }
                                })), (0, B.createElement)("div", {
                                    className: C,
                                    onKeyDown: this.handleKeyDown
                                }, (0, B.createElement)(D.default, {
                                    id: a,
                                    length: _.length,
                                    queryLength: k.length,
                                    minQueryLength: o,
                                    selectedOption: this.templateInputValue(_[S]),
                                    selectedOptionIndex: S,
                                    validChoiceMade: b,
                                    isInFocus: null !== this.state.focused,
                                    tQueryTooShort: f,
                                    tNoResults: p,
                                    tSelectedOption: h,
                                    tResults: m
                                }), x && (0, B.createElement)("span", null, (0, B.createElement)("input", {
                                    className: q,
                                    readonly: !0,
                                    tabIndex: "-1",
                                    value: x
                                })), (0, B.createElement)("input", H({
                                    "aria-expanded": w ? "true" : "false",
                                    "aria-activedescendant": !!N && a + "__option--" + y,
                                    "aria-owns": a + "__listbox",
                                    "aria-autocomplete": this.hasAutoselect() ? "both" : "list"
                                }, E, {
                                    autoComplete: "off",
                                    className: A + T + j,
                                    id: a,
                                    onClick: function(e) {
                                        return i.handleInputClick(e)
                                    },
                                    onBlur: this.handleInputBlur
                                }, {
                                    onInput: this.handleInputChange
                                }, {
                                    onFocus: this.handleInputFocus,
                                    name: s,
                                    placeholder: u,
                                    ref: function(e) {
                                        i.elementReferences[-1] = e
                                    },
                                    type: "text",
                                    role: "combobox",
                                    required: c,
                                    value: k
                                })), e, (0, B.createElement)("ul", {
                                    className: P + " " + r + " " + R,
                                    onMouseLeave: function(e) {
                                        return i.handleListMouseLeave(e)
                                    },
                                    id: a + "__listbox",
                                    role: "listbox"
                                }, _.map(function(e, t) {
                                    var n = (-1 === y ? S === t : y === t) && null === g ? " " + I + "--focused" : "",
                                        r = t % 2 ? " " + I + "--odd" : "",
                                        o = U() ? "<span id=" + a + "__option-suffix--" + t + ' style="border:0;clip:rect(0 0 0 0);height:1px;marginBottom:-1px;marginRight:-1px;overflow:hidden;padding:0;position:absolute;whiteSpace:nowrap;width:1px"> ' + (t + 1) + " of " + _.length + "</span>" : "";
                                    return (0, B.createElement)("li", {
                                        "aria-selected": y === t ? "true" : "false",
                                        className: I + n + r,
                                        dangerouslySetInnerHTML: {
                                            __html: i.templateSuggestion(e) + o
                                        },
                                        id: a + "__option--" + t,
                                        key: t,
                                        onBlur: function(e) {
                                            return i.handleOptionBlur(e, t)
                                        },
                                        onClick: function(e) {
                                            return i.handleOptionClick(e, t)
                                        },
                                        onMouseDown: i.handleOptionMouseDown,
                                        onMouseEnter: function(e) {
                                            return i.handleOptionMouseEnter(e, t)
                                        },
                                        ref: function(e) {
                                            i.elementReferences[t] = e
                                        },
                                        role: "option",
                                        tabIndex: "-1",
                                        "aria-posinset": t + 1,
                                        "aria-setsize": _.length
                                    })
                                }), O && (0, B.createElement)("li", {
                                    className: I + " " + I + "--no-results"
                                }, d())), (0, B.createElement)("span", {
                                    id: M,
                                    style: {
                                        display: "none"
                                    }
                                }, v()))
                            };
                            var a, s, u = c;

                            function c(e) {
                                var t;
                                return (t = a.call(this, e) || this).elementReferences = {}, t.state = {
                                    focused: null,
                                    hovered: null,
                                    menuOpen: !1,
                                    options: e.defaultValue ? [e.defaultValue] : [],
                                    query: e.defaultValue,
                                    validChoiceMade: !1,
                                    selected: null,
                                    ariaHint: !0
                                }, t.handleComponentBlur = t.handleComponentBlur.bind(o(o(t))), t.handleKeyDown = t.handleKeyDown.bind(o(o(t))), t.handleUpArrow = t.handleUpArrow.bind(o(o(t))), t.handleDownArrow = t.handleDownArrow.bind(o(o(t))), t.handleEnter = t.handleEnter.bind(o(o(t))), t.handlePrintableKey = t.handlePrintableKey.bind(o(o(t))), t.handleListMouseLeave = t.handleListMouseLeave.bind(o(o(t))), t.handleOptionBlur = t.handleOptionBlur.bind(o(o(t))), t.handleOptionClick = t.handleOptionClick.bind(o(o(t))), t.handleOptionFocus = t.handleOptionFocus.bind(o(o(t))), t.handleOptionMouseDown = t.handleOptionMouseDown.bind(o(o(t))), t.handleOptionMouseEnter = t.handleOptionMouseEnter.bind(o(o(t))), t.handleInputBlur = t.handleInputBlur.bind(o(o(t))), t.handleInputChange = t.handleInputChange.bind(o(o(t))), t.handleInputFocus = t.handleInputFocus.bind(o(o(t))), t.pollInputElement = t.pollInputElement.bind(o(o(t))), t.getDirectInputChanges = t.getDirectInputChanges.bind(o(o(t))), t
                            }(t.default = u).defaultProps = {
                                autoselect: !1,
                                cssNamespace: "autocomplete",
                                defaultValue: "",
                                displayMenu: "inline",
                                minLength: 0,
                                name: "input-autocomplete",
                                placeholder: "",
                                onConfirm: function() {},
                                confirmOnBlur: !0,
                                showNoOptionsFound: !0,
                                showAllValues: !1,
                                required: !1,
                                tNoResults: function() {
                                    return "No results found"
                                },
                                tAssistiveHint: function() {
                                    return "When autocomplete results are available use up and down arrows to review and enter to select.  Touch device users, explore by touch or with swipe gestures."
                                },
                                dropdownArrow: n.default
                            }
                        }, function(e, t, n) {
                            function r() {}
                            var o = n(9),
                                i = n(53),
                                a = n(28),
                                s = n(26)("IE_PROTO"),
                                u = "prototype",
                                c = function() {
                                    var e = n(15)("iframe"),
                                        t = a.length;
                                    for (e.style.display = "none", n(54).appendChild(e), e.src = "javascript:", (e = e.contentWindow.document).open(), e.write("<script>document.F=Object<\/script>"), e.close(), c = e.F; t--;) delete c[u][a[t]];
                                    return c()
                                };
                            e.exports = Object.create || function(e, t) {
                                var n;
                                return null !== e ? (r[u] = o(e), n = new r, r[u] = null, n[s] = e) : n = c(), void 0 === t ? n : i(n, t)
                            }
                        }, function(e, t, n) {
                            var a = n(8),
                                s = n(9),
                                u = n(20);
                            e.exports = n(3) ? Object.defineProperties : function(e, t) {
                                s(e);
                                for (var n, r = u(t), o = r.length, i = 0; i < o;) a.f(e, n = r[i++], t[n]);
                                return e
                            }
                        }, function(e, t, n) {
                            n = n(1).document;
                            e.exports = n && n.documentElement
                        }, function(e, t, n) {
                            var r = n(0);
                            r(r.P, "Function", {
                                bind: n(56)
                            })
                        }, function(e, t, n) {
                            "use strict";
                            var r = n(19),
                                o = n(2),
                                l = n(57),
                                d = [].slice,
                                f = {};
                            e.exports = Function.bind || function(a) {
                                function s() {
                                    var e = c.concat(d.call(arguments));
                                    if (this instanceof s) {
                                        var t = u,
                                            n = e.length,
                                            r = e;
                                        if (!(n in f)) {
                                            for (var o = [], i = 0; i < n; i++) o[i] = "a[" + i + "]";
                                            f[n] = Function("F,a", "return new F(" + o.join(",") + ")")
                                        }
                                        return f[n](t, r)
                                    }
                                    return l(u, e, a)
                                }
                                var u = r(this),
                                    c = d.call(arguments, 1);
                                return o(u.prototype) && (s.prototype = u.prototype), s
                            }
                        }, function(e, t) {
                            e.exports = function(e, t, n) {
                                var r = void 0 === n;
                                switch (t.length) {
                                    case 0:
                                        return r ? e() : e.call(n);
                                    case 1:
                                        return r ? e(t[0]) : e.call(n, t[0]);
                                    case 2:
                                        return r ? e(t[0], t[1]) : e.call(n, t[0], t[1]);
                                    case 3:
                                        return r ? e(t[0], t[1], t[2]) : e.call(n, t[0], t[1], t[2]);
                                    case 4:
                                        return r ? e(t[0], t[1], t[2], t[3]) : e.call(n, t[0], t[1], t[2], t[3])
                                }
                                return e.apply(n, t)
                            }
                        }, function(e, t, n) {
                            n(59)("match", 1, function(r, o, e) {
                                return [function(e) {
                                    "use strict";
                                    var t = r(this),
                                        n = null == e ? void 0 : e[o];
                                    return void 0 !== n ? n.call(e, t) : new RegExp(e)[o](String(t))
                                }, e]
                            })
                        }, function(e, t, n) {
                            "use strict";
                            var a = n(7),
                                s = n(16),
                                u = n(4),
                                c = n(12),
                                l = n(34);
                            e.exports = function(t, e, n) {
                                var r = l(t),
                                    n = n(c, r, "" [t]),
                                    o = n[0],
                                    i = n[1];
                                u(function() {
                                    var e = {};
                                    return e[r] = function() {
                                        return 7
                                    }, 7 != "" [t](e)
                                }) && (s(String.prototype, t, o), a(RegExp.prototype, r, 2 == e ? function(e, t) {
                                    return i.call(e, this, t)
                                } : function(e) {
                                    return i.call(e, this)
                                }))
                            }
                        }, function(e, t, n) {
                            "use strict";
                            t.__esModule = !0, t.default = void 0, n(36);
                            var o, r, h = n(5),
                                n = (o = h.Component, n = o, (r = i).prototype = Object.create(n.prototype), (r.prototype.constructor = r).__proto__ = n, (r = i.prototype).componentWillMount = function() {
                                    var n, r, e = this;
                                    this.debounceStatusUpdate = (n = function() {
                                        var t;
                                        e.state.debounced || (t = !e.props.isInFocus || e.props.validChoiceMade, e.setState(function(e) {
                                            return {
                                                bump: !e.bump,
                                                debounced: !0,
                                                silenced: t
                                            }
                                        }))
                                    }, function() {
                                        var e = this,
                                            t = arguments;
                                        clearTimeout(r), r = setTimeout(function() {
                                            r = null, n.apply(e, t)
                                        }, 1400)
                                    })
                                }, r.componentWillReceiveProps = function(e) {
                                    e.queryLength, this.setState({
                                        debounced: !1
                                    })
                                }, r.render = function() {
                                    var e = this.props,
                                        t = e.id,
                                        n = e.length,
                                        r = e.queryLength,
                                        o = e.minQueryLength,
                                        i = e.selectedOption,
                                        a = e.selectedOptionIndex,
                                        s = e.tQueryTooShort,
                                        u = e.tNoResults,
                                        c = e.tSelectedOption,
                                        e = e.tResults,
                                        l = this.state,
                                        d = l.bump,
                                        f = l.debounced,
                                        l = l.silenced,
                                        r = r < o,
                                        p = 0 === n,
                                        c = i ? c(i, n, a) : "",
                                        i = r ? s(o) : p ? u() : e(n, c);
                                    return this.debounceStatusUpdate(), (0, h.createElement)("div", {
                                        style: {
                                            border: "0",
                                            clip: "rect(0 0 0 0)",
                                            height: "1px",
                                            marginBottom: "-1px",
                                            marginRight: "-1px",
                                            overflow: "hidden",
                                            padding: "0",
                                            position: "absolute",
                                            whiteSpace: "nowrap",
                                            width: "1px"
                                        }
                                    }, (0, h.createElement)("div", {
                                        id: t + "__status--A",
                                        role: "status",
                                        "aria-atomic": "true",
                                        "aria-live": "polite"
                                    }, !l && f && d ? i : ""), (0, h.createElement)("div", {
                                        id: t + "__status--B",
                                        role: "status",
                                        "aria-atomic": "true",
                                        "aria-live": "polite"
                                    }, l || !f || d ? "" : i))
                                }, i);

                            function i() {
                                for (var e, t = arguments.length, n = new Array(t), r = 0; r < t; r++) n[r] = arguments[r];
                                return (e = o.call.apply(o, [this].concat(n)) || this).state = {
                                    bump: !1,
                                    debounced: !1
                                }, e
                            }(t.default = n).defaultProps = {
                                tQueryTooShort: function(e) {
                                    return "Type in " + e + " or more characters for results"
                                },
                                tNoResults: function() {
                                    return "No search results"
                                },
                                tSelectedOption: function(e, t, n) {
                                    return e + " " + (n + 1) + " of " + t + " is highlighted"
                                },
                                tResults: function(e, t) {
                                    return e + " " + (1 === e ? "result" : "results") + " " + (1 === e ? "is" : "are") + " available. " + t
                                }
                            }
                        }, function(e, t, n) {
                            "use strict";
                            t.__esModule = !0, t.default = void 0;
                            var r = n(5);
                            t.default = function(e) {
                                e = e.className;
                                return (0, r.createElement)("svg", {
                                    version: "1.1",
                                    xmlns: "http://www.w3.org/2000/svg",
                                    className: e,
                                    focusable: "false"
                                }, (0, r.createElement)("g", {
                                    stroke: "none",
                                    fill: "none",
                                    "fill-rule": "evenodd"
                                }, (0, r.createElement)("polygon", {
                                    fill: "#000000",
                                    points: "0 0 22 0 11 17"
                                })))
                            }
                        }], r = {}, o.m = n, o.c = r, o.d = function(e, t, n) {
                            o.o(e, t) || Object.defineProperty(e, t, {
                                enumerable: !0,
                                get: n
                            })
                        }, o.r = function(e) {
                            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                                value: "Module"
                            }), Object.defineProperty(e, "__esModule", {
                                value: !0
                            })
                        }, o.t = function(t, e) {
                            if (1 & e && (t = o(t)), 8 & e) return t;
                            if (4 & e && "object" == g(t) && t && t.__esModule) return t;
                            var n = Object.create(null);
                            if (o.r(n), Object.defineProperty(n, "default", {
                                    enumerable: !0,
                                    value: t
                                }), 2 & e && "string" != typeof t)
                                for (var r in t) o.d(n, r, function(e) {
                                    return t[e]
                                }.bind(null, r));
                            return n
                        }, o.n = function(e) {
                            var t = e && e.__esModule ? function() {
                                return e.default
                            } : function() {
                                return e
                            };
                            return o.d(t, "a", t), t
                        }, o.o = function(e, t) {
                            return Object.prototype.hasOwnProperty.call(e, t)
                        }, o.p = "/", o(o.s = 37).default;

                        function o(e) {
                            if (r[e]) return r[e].exports;
                            var t = r[e] = {
                                i: e,
                                l: !1,
                                exports: {}
                            };
                            return n[e].call(t.exports, t, t.exports, o), t.l = !0, t.exports
                        }
                        var n, r
                    }, "object" == g(n) && "object" == g(e) ? e.exports = t() : void 0 !== (t = "function" == typeof(t = t) ? t.apply(n, []) : t) && (e.exports = t)
                }.call(this, t(2)(e))
            }, function(e, t, n) {
                "use strict";
                n.r(t);
                var r = n(0),
                    i = n.n(r);
                t.default = function() {
                    var t = document.getElementById("search"),
                        e = document.getElementById("search-field"),
                        n = document.getElementById("autocomplete-container"),
                        r = window.NHSUK_SETTINGS && window.NHSUK_SETTINGS.SUGGESTIONS_TEST_HOST || "https://api.nhs.uk/site-search/Autocomplete",
                        o = window.NHSUK_SETTINGS && window.NHSUK_SETTINGS.SEARCH_TEST_HOST || "https://www.nhs.uk/search/";
                    e && n && (e.parentNode.removeChild(e), i()({
                        confirmOnBlur: !1,
                        element: n,
                        id: "search-field",
                        minLength: 2,
                        name: e.name,
                        onConfirm: function(e) {
                            window.location.href = "".concat(o, "?q=").concat(e)
                        },
                        placeholder: e.placeholder,
                        showNoOptionsFound: !1,
                        source: function(e, t) {
                            var e = "".concat(r, "?q=").concat(e, "&api-version=1"),
                                n = new XMLHttpRequest;
                            n.open("GET", e), n.onload = function() {
                                var e;
                                200 === n.status && (e = JSON.parse(n.responseText).map(function(e) {
                                    return e.query
                                }), t(e))
                            }, n.send()
                        },
                        templates: {
                            suggestion: function(e) {
                                var t = 36 < e.length ? "..." : "",
                                    e = e.substring(0, 36) + t;
                                return '\n      <svg class="nhsuk-icon nhsuk-icon__search" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M19.71 18.29l-4.11-4.1a7 7 0 1 0-1.41 1.41l4.1 4.11a1 1 0 0 0 1.42 0 1 1 0 0 0 0-1.42zM5 10a5 5 0 1 1 5 5 5 5 0 0 1-5-5z"></path></svg>\n      '.concat(e, "\n    ")
                            }
                        }
                    }), t && t.addEventListener("keyup", function(e) {
                        "Enter" === e.key && "search-field" === document.activeElement.id && t.submit()
                    }))
                }
            }, function(e, t) {
                e.exports = function(e) {
                    return e.webpackPolyfill || (e.deprecate = function() {}, e.paths = [], e.children || (e.children = []), Object.defineProperty(e, "loaded", {
                        enumerable: !0,
                        get: function() {
                            return e.l
                        }
                    }), Object.defineProperty(e, "id", {
                        enumerable: !0,
                        get: function() {
                            return e.i
                        }
                    }), e.webpackPolyfill = 1), e
                }
            }], r = {}, o.m = n, o.c = r, o.d = function(e, t, n) {
                o.o(e, t) || Object.defineProperty(e, t, {
                    enumerable: !0,
                    get: n
                })
            }, o.r = function(e) {
                "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                    value: "Module"
                }), Object.defineProperty(e, "__esModule", {
                    value: !0
                })
            }, o.t = function(t, e) {
                if (1 & e && (t = o(t)), 8 & e) return t;
                if (4 & e && "object" == i(t) && t && t.__esModule) return t;
                var n = Object.create(null);
                if (o.r(n), Object.defineProperty(n, "default", {
                        enumerable: !0,
                        value: t
                    }), 2 & e && "string" != typeof t)
                    for (var r in t) o.d(n, r, function(e) {
                        return t[e]
                    }.bind(null, r));
                return n
            }, o.n = function(e) {
                var t = e && e.__esModule ? function() {
                    return e.default
                } : function() {
                    return e
                };
                return o.d(t, "a", t), t
            }, o.o = function(e, t) {
                return Object.prototype.hasOwnProperty.call(e, t)
            }, o.p = "", o(o.s = 1);

            function o(e) {
                if (r[e]) return r[e].exports;
                var t = r[e] = {
                    i: e,
                    l: !1,
                    exports: {}
                };
                return n[e].call(t.exports, t, t.exports, o), t.l = !0, t.exports
            }
            var n, r
        }, "object" == i(n) && "object" == i(e) ? e.exports = t() : void 0 !== (t = "function" == typeof(t = t) ? t.apply(n, []) : t) && (e.exports = t)
    }.call(this, t(0)(e))
}, function(e, t) {
    function o(e, t) {
        (null == t || t > e.length) && (t = e.length);
        for (var n = 0, r = new Array(t); n < t; n++) r[n] = e[n];
        return r
    }
    String.prototype.includes || Object.assign(String.prototype, {
        includes: function(e) {
            return -1 !== this.indexOf(e)
        }
    });

    function u(e) {
        var t = e.link,
            n = e.content,
            e = e.listItem;
        r.forEach(function(e) {
            e = d(e);
            p(e)
        }), e.classList.add(l), t.setAttribute("aria-selected", "true"), n.setAttribute("aria-hidden", "false"), f(n)
    }

    function c() {
        var e = 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : null;
        window.history.replaceState && (e = e ? e.getAttribute("href").substring(1) : "", e = n(e), window.history.replaceState(null, "", e))
    }
    var r = document.querySelectorAll(".app-guides-nav__label"),
        i = document.querySelector(".app-guides-nav__spacer"),
        l = "app-guides-nav__item--selected",
        d = function(e) {
            return {
                content: e.nextElementSibling,
                link: e,
                listItem: e.parentElement
            }
        },
        f = function(e) {
            e = e, t = getComputedStyle(e), e.clientWidth, e = e.clientHeight;
            var t, e = [e -= parseFloat(t.paddingTop) + parseFloat(t.paddingBottom), (parseFloat(t.paddingLeft), parseFloat(t.paddingRight))][0];
            i.style.height = "".concat(e, "px")
        },
        p = function(e) {
            var t = e.link,
                n = e.content,
                r = e.listItem,
                o = !(1 < arguments.length && void 0 !== arguments[1]) || arguments[1];
            r.classList.remove(l), t.setAttribute("aria-selected", "false"), n.setAttribute("aria-hidden", "true"), o && (i.style.height = "0px")
        },
        n = function(e) {
            t = window.location.href.split("?"), n = 2;
            var t = function(e) {
                    if (Array.isArray(e)) return e
                }(t) || function(e, t) {
                    var n = null == e ? null : "undefined" != typeof Symbol && e[Symbol.iterator] || e["@@iterator"];
                    if (null != n) {
                        var r, o, i = [],
                            a = !0,
                            s = !1;
                        try {
                            for (n = n.call(e); !(a = (r = n.next()).done) && (i.push(r.value), !t || i.length !== t); a = !0);
                        } catch (e) {
                            s = !0, o = e
                        } finally {
                            try {
                                a || null == n.return || n.return()
                            } finally {
                                if (s) throw o
                            }
                        }
                        return i
                    }
                }(t, n) || function(e, t) {
                    if (e) {
                        if ("string" == typeof e) return o(e, t);
                        var n = Object.prototype.toString.call(e).slice(8, -1);
                        return "Map" === (n = "Object" === n && e.constructor ? e.constructor.name : n) || "Set" === n ? Array.from(e) : "Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? o(e, t) : void 0
                    }
                }(t, n) || function() {
                    throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                }(),
                n = t[0],
                t = t[1],
                t = void 0 === t ? "" : t;
            if (t.length) {
                var t = t.split("&").filter(function(e) {
                        return !e.includes("tabname")
                    }).join("&"),
                    r = t.length ? "".concat(n, "?").concat(t) : n;
                if (!e) return r;
                t = t.length ? "&" : "?";
                return "".concat(r).concat(t).concat(e)
            }
            return "".concat(n, "?").concat(e)
        };
    window.addEventListener("DOMContentLoaded", function() {
        r.forEach(function(e, t) {
            var n, r, o, i, a, s, e = d(e);
            t = t, a = e.link, s = e.content, a.setAttribute("aria-controls", "app-guides-nav__contents-".concat(t)), a.setAttribute("id", "app-guides-nav__label-".concat(t)), s.setAttribute("id", "app-guides-nav__contents-".concat(t)), r = (n = e).link, o = n.listItem, i = n.content, r && r.addEventListener("click", function(e) {
                e.preventDefault(), o.classList.contains(l) ? (p(n), c()) : (u(n), c(r))
            }), i && i.addEventListener("click", function() {
                setTimeout(function() {
                    f(i)
                }, 1)
            }), s = (a = e).link.getAttribute("href").substring(1), window.location.href.includes(s) ? u(a) : p(a, !1)
        })
    })
}, function(e, t) {
    var n = document.getElementsByClassName("video-js");
    if (n)
        for (var r = 0; r < n.length; r++) {
            var o = n[r].id;
            videojs.getPlayer(o).ready(function() {
                var r = this,
                    e = document.createElement("div"),
                    t = (e.innerHTML = "<img src='https://assets.nhs.uk/nhsuk-cms/images/video-error-message.png'>", {}),
                    o = (t.content = e, new(videojs.getComponent("ModalDialog"))(r, t));
                r.addChild(o), r.on("error", function(e) {
                    var t = r.error().code,
                        n = r.duration();
                    ("4" === t && 0 === n || "4" === t && Number.isNaN(n)) && (r.errorDisplay.hide(), o.open())
                }), o.on("modalclose", function() {
                    r.errorDisplay.show()
                })
            })
        }
}, function(e, t) {
    window.addEventListener("beforeprint", function() {
        document.querySelectorAll("details").forEach(function(e) {
            return e.setAttribute("open", "true")
        })
    })
}, function(e, t) {
    NodeList.prototype.forEach || (NodeList.prototype.forEach = Array.prototype.forEach), Array.prototype.includes || Object.defineProperty(Array.prototype, "includes", {
        enumerable: !1,
        value: function(t) {
            return 0 < this.filter(function(e) {
                return e === t
            }).length
        }
    }), Element.prototype.matches || (Element.prototype.matches = Element.prototype.msMatchesSelector || Element.prototype.webkitMatchesSelector), Element.prototype.closest || (Element.prototype.closest = function(e) {
        var t = this;
        do {
            if (Element.prototype.matches.call(t, e)) return t
        } while (null !== (t = t.parentElement || t.parentNode) && 1 === t.nodeType);
        return null
    })
}, function(e, t, n) {
    "use strict";
    n.r(t);
    t = n(1), t = n.n(t);

    function r(t, e) {
        var n, r = Object.keys(t);
        return Object.getOwnPropertySymbols && (n = Object.getOwnPropertySymbols(t), e && (n = n.filter(function(e) {
            return Object.getOwnPropertyDescriptor(t, e).enumerable
        })), r.push.apply(r, n)), r
    }

    function o(t) {
        for (var e = 1; e < arguments.length; e++) {
            var n = null != arguments[e] ? arguments[e] : {};
            e % 2 ? r(Object(n), !0).forEach(function(e) {
                i(t, e, n[e])
            }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(t, Object.getOwnPropertyDescriptors(n)) : r(Object(n)).forEach(function(e) {
                Object.defineProperty(t, e, Object.getOwnPropertyDescriptor(n, e))
            })
        }
        return t
    }

    function i(e, t, n) {
        return t in e ? Object.defineProperty(e, t, {
            value: n,
            enumerable: !0,
            configurable: !0,
            writable: !0
        }) : e[t] = n, e
    }

    function a(e, t) {
        (null == t || t > e.length) && (t = e.length);
        for (var n = 0, r = new Array(t); n < t; n++) r[n] = e[n];
        return r
    }

    function u(e, t) {
        var n = new Date;
        n.setTime(n.getTime() + 24 * t * 60 * 60 * 1e3), document.cookie = "nhsuk-banner-".concat(e, "=true;expires=").concat(n.toUTCString(), ";path=/")
    }

    function c(e) {
        return Boolean((e = "nhsuk-banner-".concat(e), decodeURIComponent(document.cookie).split("; ").reduce(function(e, t) {
            t = t.split("="), n = 2;
            var t = function(e) {
                    if (Array.isArray(e)) return e
                }(t) || function(e, t) {
                    var n = null == e ? null : "undefined" != typeof Symbol && e[Symbol.iterator] || e["@@iterator"];
                    if (null != n) {
                        var r, o, i = [],
                            a = !0,
                            s = !1;
                        try {
                            for (n = n.call(e); !(a = (r = n.next()).done) && (i.push(r.value), !t || i.length !== t); a = !0);
                        } catch (e) {
                            s = !0, o = e
                        } finally {
                            try {
                                a || null == n.return || n.return()
                            } finally {
                                if (s) throw o
                            }
                        }
                        return i
                    }
                }(t, n) || function(e, t) {
                    if (e) {
                        if ("string" == typeof e) return a(e, t);
                        var n = Object.prototype.toString.call(e).slice(8, -1);
                        return "Map" === (n = "Object" === n && e.constructor ? e.constructor.name : n) || "Set" === n ? Array.from(e) : "Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? a(e, t) : void 0
                    }
                }(t, n) || function() {
                    throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                }(),
                n = t[0],
                t = t[1];
            return o(o({}, e), {}, i({}, n.trim(), t))
        }, {})[e] || ""))
    }

    function l(e, t) {
        (null == t || t > e.length) && (t = e.length);
        for (var n = 0, r = new Array(t); n < t; n++) r[n] = e[n];
        return r
    }

    function d() {
        document.getElementById("app-feedback-banner").setAttribute("style", "display: none")
    }

    function f(e) {
        var t = window.location.href.toLowerCase();
        return 0 <= e.toLowerCase().split(";").indexOf(t)
    }

    function s(e) {
        var t, n, r, o, i, a, s = e.find(function(e) {
            return "Alert" === e.Style
        });
        s || (!(e = e.find(function(e) {
            return "Default" === e.Style
        })) || (a = (t = e).Including, o = t.Excluding, c(t.BannerId) || (t = a, f(o) || 0 !== t.length && !f(t))) || (s = e)), s && (n = s, i = document.createElement("div"), a = "Alert" === n.Style ? '<div class="app-global-alert" id="app-global-alert" role="complementary">\n<div class="nhsuk-width-container">\n<div class="nhsuk-grid-row">\n<div class="nhsuk-grid-column-full">\n<div class="app-global-alert__content">\n<div class="app-global-alert__message">[Content]</div>\n</div></div></div></div></div>' : '<div class="app-feedback-banner" id="app-feedback-banner">\n<div class="nhsuk-width-container">\n<div class="nhsuk-grid-row">\n<div class="nhsuk-grid-column-full">\n<div class="app-feedback-banner__content">\n<h2 class="app-feedback-banner__heading">[Invitation1]</h2>\n<p class="app-feedback-banner__message nhsuk-u-margin-bottom-2">\n<a href="[BannerUrl]" id="AgreeButton" target="_blank">Take our survey (opens new page)</a>\n</p>\n<p class="app-feedback-banner__message nhsuk-u-margin-bottom-4">\n<a href="#" id="DisagreeButton">I do not want to take this survey</a>\n</p>\n<p class="nhsuk-u-margin-bottom-0">We\'ll use a cookie to save your choice.</p>\n<button class="app-feedback-banner__close" id="app-feedback-banner-close" type="button">Hide<span class="nhsuk-u-visually-hidden"> feedback invite</span></button>\n</div></div></div></div></div>', i.innerHTML = a.replace(/\[(\w*)\]/g, function(e, t) {
            return n[t] || ""
        }), "Alert" === n.Style ? (a = document.getElementsByTagName("header"), o = 1, (a = (function(e) {
            if (Array.isArray(e)) return e
        }(a) || function(e, t) {
            var n = null == e ? null : "undefined" != typeof Symbol && e[Symbol.iterator] || e["@@iterator"];
            if (null != n) {
                var r, o, i = [],
                    a = !0,
                    s = !1;
                try {
                    for (n = n.call(e); !(a = (r = n.next()).done) && (i.push(r.value), !t || i.length !== t); a = !0);
                } catch (e) {
                    s = !0, o = e
                } finally {
                    try {
                        a || null == n.return || n.return()
                    } finally {
                        if (s) throw o
                    }
                }
                return i
            }
        }(a, o) || function(e, t) {
            if (e) {
                if ("string" == typeof e) return l(e, t);
                var n = Object.prototype.toString.call(e).slice(8, -1);
                return "Map" === (n = "Object" === n && e.constructor ? e.constructor.name : n) || "Set" === n ? Array.from(e) : "Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? l(e, t) : void 0
            }
        }(a, o) || function() {
            throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
        }())[0]).parentElement.insertBefore(i.firstChild, a.nextElementSibling)) : "Default" === n.Style && (i.firstChild.style.display = "block", r = document.getElementById("nhsuk-footer"), setTimeout(function() {
            r.insertBefore(i.firstChild, r.childNodes[0]), document.getElementById("DisagreeButton").addEventListener("click", function(e) {
                e.preventDefault(), d(), u(n.BannerId, 99)
            }, !1), document.getElementById("AgreeButton").addEventListener("click", function() {
                d(), u(n.BannerId, 99)
            }, !1), document.getElementById("app-feedback-banner-close").addEventListener("click", function() {
                d()
            }, !1)
        }, 3e3)))
    }
    document.addEventListener("DOMContentLoaded", function() {
        var e, t;
        window.NHSUK_SETTINGS.EMERGENCY_ALERT_DISABLED || (e = /[?&]test/.test(window.location.href) ? window.NHSUK_SETTINGS.BANNER_TEST_API_URL : window.NHSUK_SETTINGS.BANNER_API_URL, (t = new XMLHttpRequest).open("GET", e, !0), t.setRequestHeader("Content-Type", "application/json; charset=UTF-8"), t.onreadystatechange = function() {
            4 === t.readyState && (200 === t.status && s(JSON.parse(t.responseText)), s([]))
        }, t.send())
    }), n(3), n(4), navigator.userAgent.includes("nhsapp-") && (document.getElementsByClassName("nhsuk-footer")[0].style.display = "none", document.getElementsByClassName("nhsuk-breadcrumb")[0].style.display = "none", document.getElementsByClassName("nhsuk-header")[0].style.display = "none"), n(5);

    function p() {
        var n = !1,
            r = document.querySelector(".beta-nhsuk-navigation"),
            o = document.querySelector(".beta-nhsuk-header__navigation-list"),
            i = document.createElement("ul"),
            a = document.querySelector(".beta-nhsuk-header__menu-toggle"),
            t = document.createElement("button"),
            s = document.querySelector(".beta-mobile-menu-container"),
            u = [],
            c = document.body.offsetWidth;

        function e(r, e) {
            var o, i = this,
                a = 1 < arguments.length && void 0 !== e ? e : 100;
            return function() {
                for (var e = arguments.length, t = new Array(e), n = 0; n < e; n++) t[n] = arguments[n];
                clearTimeout(o), o = setTimeout(function() {
                    r.apply(i, t)
                }, a)
            }
        }

        function l() {
            for (var e = 0, t = 0; t < o.children.length; t++) e += o.children[t].offsetWidth, u[t] = e
        }

        function d() {
            n = !1, i.classList.add("js-hidden"), r.style.marginBottom = 0, a.setAttribute("aria-expanded", "false"), a.focus(), t.removeEventListener("click", d), document.removeEventListener("keydown", f)
        }

        function f(e) {
            "Escape" === e.key && d()
        }

        function p() {
            var e = r.offsetWidth,
                t = o.children.length;
            if (e < u[t - 1]) {
                if (a.classList.add("js-show"), s.classList.add("js-show"), 2 === t) return;
                for (; e < u[t - 1];) i.insertBefore(o.children[t - 2], i.firstChild), --t
            } else if (e > u[t])
                for (; e > u[t];) o.insertBefore(i.removeChild(i.firstChild), s), t += 1;
            i.children.length || (a.classList.remove("js-show"), s.classList.remove("js-show")), document.body.offsetWidth !== c && n && d()
        }

        function h() {
            90 === window.orientation && setTimeout(function() {
                l(), p()
            }, 200)
        }
        s.appendChild(i), i.classList.add("beta-nhsuk-header__drop-down", "js-hidden"), l(), p(), h(), window.addEventListener("resize", e(l)), window.addEventListener("resize", e(p)), window.addEventListener("orientationchange", h), a.addEventListener("click", function() {
            var e;
            n ? d() : (n = !0, i.classList.remove("js-hidden"), e = i.offsetHeight, r.style.marginBottom = "".concat(e, "px"), a.setAttribute("aria-expanded", "true"), document.addEventListener("keydown", f), t.addEventListener("click", d))
        })
    }

    function h(e, t) {
        var n;
        e && t && (n = "true" === e.getAttribute(t) ? "false" : "true", e.setAttribute(t, n))
    }

    function m() {
        var e;
        "boolean" != typeof document.createElement("details").open && (e = document.querySelectorAll("details")).length && e.forEach(function(e, t) {
            var n, r, o;
            e.hasAttribute("nhsuk-polyfilled") || (t = t, (n = e).setAttribute("nhsuk-polyfilled", "true"), n.id || n.setAttribute("id", "nhsuk-details".concat(t)), (r = document.querySelector("#".concat(n.id, " .nhsuk-details__text"))).id || r.setAttribute("id", "nhsuk-details__text".concat(t)), (o = document.querySelector("#".concat(n.id, " .nhsuk-details__summary"))).setAttribute("role", "button"), o.setAttribute("aria-controls", r.id), o.setAttribute("tabIndex", "0"), !0 == (null !== n.getAttribute("open")) ? (o.setAttribute("aria-expanded", "true"), r.setAttribute("aria-hidden", "false")) : (o.setAttribute("aria-expanded", "false"), r.setAttribute("aria-hidden", "true"), r.style.display = "none"), o.addEventListener("click", function() {
                h(o, "aria-expanded"), h(r, "aria-hidden"), r.style.display = "true" === r.getAttribute("aria-hidden") ? "none" : "", n.hasAttribute("open") ? n.removeAttribute("open") : n.setAttribute("open", "open")
            }), o.addEventListener("keydown", function(e) {
                13 !== e.keyCode && 32 !== e.keyCode || (e.preventDefault(), o.click())
            }))
        })
    }

    function v(e) {
        e.form.querySelectorAll('input[type="checkbox"]').forEach(function(e) {
            return y(e, "nhsuk-checkboxes__conditional--hidden")
        })
    }

    function b() {
        function t(e) {
            var t, n;
            y(e.target, "nhsuk-checkboxes__conditional--hidden"), e.target.checked && (e.target.hasAttribute("data-checkbox-exclusive") ? ((t = e.target).form.querySelectorAll('input[type="checkbox"][data-checkbox-exclusive-group="'.concat(t.getAttribute("data-checkbox-exclusive-group"), '"]')).forEach(function(e) {
                t.form === e.form && e !== t && (e.checked = !1)
            }), v(t)) : ((n = e.target).form.querySelectorAll('input[type="checkbox"][data-checkbox-exclusive][data-checkbox-exclusive-group="'.concat(n.getAttribute("data-checkbox-exclusive-group"), '"]')).forEach(function(e) {
                n.form === e.form && (e.checked = !1)
            }), v(n)))
        }
        var e = document.querySelectorAll(".nhsuk-checkboxes .nhsuk-checkboxes__input");
        "onpageshow" in window ? window.addEventListener("pageshow", function() {
            return e.forEach(v)
        }) : window.addEventListener("DOMContentLoaded", function() {
            return e.forEach(v)
        }), e.forEach(v), e.forEach(function(e) {
            e.addEventListener("change", t)
        })
    }
    var y = function(e, t) {
        var n;
        e && t && (n = e.getAttribute("aria-controls")) && (n = document.getElementById(n)) && (e.checked ? (n.classList.remove(t), e.setAttribute("aria-expanded", !0)) : (n.classList.add(t), e.setAttribute("aria-expanded", !1)))
    };

    function g(e) {
        ! function(e) {
            if ("A" === e.tagName && !1 !== e.href) {
                var t, e = document.querySelector(e.hash);
                if (e) return (t = function(e) {
                    var t = e.closest("fieldset");
                    if (t) {
                        t = t.getElementsByTagName("legend");
                        if (t.length) {
                            t = t[0];
                            if ("checkbox" === e.type || "radio" === e.type) return t;
                            var n = t.getBoundingClientRect().top,
                                r = e.getBoundingClientRect();
                            if (r.height && window.innerHeight && r.top + r.height - n < window.innerHeight / 2) return t
                        }
                    }
                    return document.querySelector("label[for='".concat(e.getAttribute("id"), "']")) || e.closest("label")
                }(e)) && (t.scrollIntoView(), e.focus({
                    preventScroll: !0
                }), 1)
            }
        }(e.target) || e.preventDefault()
    }
    var w = n(2),
        _ = n.n(w);

    function k(e, t) {
        for (var n = 0; n < t.length; n++) {
            var r = t[n];
            r.enumerable = r.enumerable || !1, r.configurable = !0, "value" in r && (r.writable = !0), Object.defineProperty(e, r.key, r)
        }
    }
    w = [{
        key: "getHref",
        value: function(e) {
            e = e.getAttribute("href");
            return e.slice(e.indexOf("#"), e.length)
        }
    }], k((S = x).prototype, [{
        key: "init",
        value: function() {
            "function" == typeof window.matchMedia && this.responsive ? this.setupResponsiveChecks() : this.setup()
        }
    }, {
        key: "setupResponsiveChecks",
        value: function() {
            this.mql = window.matchMedia("(min-width: 641px)"), this.mql.addEventListener("change", this.checkMode.bind(this)), this.checkMode()
        }
    }, {
        key: "checkMode",
        value: function() {
            this.mql.matches ? this.setup() : this.teardown()
        }
    }, {
        key: "setup",
        value: function() {
            var t = this,
                e = this.$module,
                n = this.$tabs,
                r = e.querySelector(".".concat(this.namespace, "__list")),
                o = e.querySelectorAll(".".concat(this.namespace, "__list-item"));
            n && r && o && (r.setAttribute("role", "tablist"), o.forEach(function(e) {
                e.setAttribute("role", "presentation")
            }), n.forEach(function(e) {
                t.setAttributes(e), e.boundTabClick = t.onTabClick.bind(t), e.boundTabKeydown = t.onTabKeydown.bind(t), e.addEventListener("click", e.boundTabClick, !0), e.addEventListener("keydown", e.boundTabKeydown, !0), t.hideTab(e)
            }), r = this.getTab(window.location.hash) || this.$tabs[0], this.showTab(r), this.historyEnabled && (e.boundOnHashChange = this.onHashChange.bind(this), window.addEventListener("hashchange", e.boundOnHashChange, !0)))
        }
    }, {
        key: "teardown",
        value: function() {
            var t = this,
                e = this.$module,
                n = this.$tabs,
                r = e.querySelector(".".concat(this.namespace, "__list")),
                o = e.querySelectorAll(".".concat(this.namespace, "__list-item"));
            n && r && o && (r.removeAttribute("role"), o.forEach(function(e) {
                e.removeAttribute("role", "presentation")
            }), n.forEach(function(e) {
                e.removeEventListener("click", e.boundTabClick, !0), e.removeEventListener("keydown", e.boundTabKeydown, !0), t.unsetAttributes(e)
            }), this.historyEnabled && window.removeEventListener("hashchange", e.boundOnHashChange, !0))
        }
    }, {
        key: "onHashChange",
        value: function() {
            var e, t = window.location.hash,
                t = this.getTab(t);
            t && (this.changingHash ? this.changingHash = !1 : (e = this.getCurrentTab(), this.hideTab(e), this.showTab(t), t.focus()))
        }
    }, {
        key: "hideTab",
        value: function(e) {
            this.unhighlightTab(e), this.hidePanel(e)
        }
    }, {
        key: "showTab",
        value: function(e) {
            this.highlightTab(e), this.showPanel(e)
        }
    }, {
        key: "getTab",
        value: function(e) {
            return this.$module.querySelector(".".concat(this.namespace, '__tab[href="').concat(e, '"]'))
        }
    }, {
        key: "setAttributes",
        value: function(e) {
            var t = x.getHref(e).slice(1),
                t = (e.setAttribute("id", "tab_".concat(t)), e.setAttribute("role", "tab"), e.setAttribute("aria-controls", t), e.setAttribute("aria-selected", "false"), e.setAttribute("tabindex", "-1"), this.getPanel(e));
            t.setAttribute("role", "tabpanel"), t.setAttribute("aria-labelledby", e.id), t.classList.add(this.jsHiddenClass)
        }
    }, {
        key: "unsetAttributes",
        value: function(e) {
            e.removeAttribute("id"), e.removeAttribute("role"), e.removeAttribute("aria-controls"), e.removeAttribute("aria-selected"), e.removeAttribute("tabindex");
            e = this.getPanel(e);
            e.removeAttribute("role"), e.removeAttribute("aria-labelledby"), e.removeAttribute("tabindex"), e.classList.remove(this.jsHiddenClass)
        }
    }, {
        key: "onTabClick",
        value: function(e) {
            var t = this.$module,
                n = (e.target.classList.contains("".concat(this.namespace, "__tab")) || e.stopPropagation(), e.preventDefault(), e.target),
                r = this.getCurrentTab(),
                o = !1;
            0 === e.screenX && (o = !0);
            for (var i = t.querySelectorAll(".".concat(this.namespace, "__panel")), a = 0; a < i.length; a++) i[a].classList.contains("".concat(this.namespace, "__panel--hidden")) || i[a].classList.add("".concat(this.namespace, "__panel--hidden"));
            for (var s = t.querySelectorAll(".".concat(this.namespace, "__list-item--selected")), u = 0; u < s.length; u++) s[u].classList.remove("".concat(this.namespace, "__list-item--selected"));
            this.hideTab(r), this.showTab(n), this.createHistoryEntry(n), o && this.getPanel(r).querySelector("img").focus()
        }
    }, {
        key: "createHistoryEntry",
        value: function(e) {
            var t, n;
            this.historyEnabled && (n = (t = this.getPanel(e)).id, t.id = "", this.changingHash = !0, window.location.hash = x.getHref(e).slice(1), t.id = n)
        }
    }, {
        key: "onTabKeydown",
        value: function(e) {
            switch (e.keyCode) {
                case this.keys.left:
                case this.keys.up:
                    this.activatePreviousTab(), e.preventDefault();
                    break;
                case this.keys.right:
                case this.keys.down:
                    this.activateNextTab(), e.preventDefault()
            }
        }
    }, {
        key: "activateNextTab",
        value: function() {
            var e, t = this.getCurrentTab(),
                n = t.parentNode.nextElementSibling;
            (e = n ? n.querySelector(".".concat(this.namespace, "__tab")) : e) && (this.unhighlightTab(t), this.highlightTab(e), e.focus(), this.createHistoryEntry(e))
        }
    }, {
        key: "activatePreviousTab",
        value: function() {
            var e, t = this.getCurrentTab(),
                n = t.parentNode.previousElementSibling;
            (e = n ? n.querySelector(".".concat(this.namespace, "__tab")) : e) && (this.unhighlightTab(t), this.highlightTab(e), e.focus(), this.createHistoryEntry(e))
        }
    }, {
        key: "getPanel",
        value: function(e) {
            return this.$module.querySelector(x.getHref(e))
        }
    }, {
        key: "showPanel",
        value: function(e) {
            var t = this.getPanel(e);
            t.classList.remove(this.jsHiddenClass), t.dispatchEvent(this.showEvent), e.parentNode.classList.add("".concat(this.namespace, "__list-item--selected"))
        }
    }, {
        key: "hidePanel",
        value: function(e) {
            var e = this.getPanel(e),
                t = e.querySelector(".nhsuk-details__summary");
            1 == (null !== e.querySelector("details").getAttribute("open")) && t.click(), e.classList.add(this.jsHiddenClass), e.dispatchEvent(this.hideEvent)
        }
    }, {
        key: "unhighlightTab",
        value: function(e) {
            e.setAttribute("aria-selected", "false"), e.parentNode.classList.remove("".concat(this.namespace, "__list-item--active")), e.setAttribute("tabindex", "-1")
        }
    }, {
        key: "highlightTab",
        value: function(e) {
            e.setAttribute("aria-selected", "true"), e.parentNode.classList.add("".concat(this.namespace, "__list-item--active")), e.setAttribute("tabindex", "0")
        }
    }, {
        key: "getCurrentTab",
        value: function() {
            return this.$module.querySelector(".".concat(this.namespace, "__list-item--active .").concat(this.namespace, "__tab"))
        }
    }]), k(S, w), Object.defineProperty(S, "prototype", {
        writable: !1
    });
    var S, E = x;

    function x(e, t, n, r) {
        if (!(this instanceof x)) throw new TypeError("Cannot call a class as a function");
        this.$module = e, this.namespace = t, this.responsive = n, this.historyEnabled = r, this.$tabs = e.querySelectorAll(".".concat(this.namespace, "__tab")), this.keys = {
            down: 40,
            left: 37,
            right: 39,
            up: 38
        }, this.jsHiddenClass = "".concat(this.namespace, "__panel--hidden"), this.showEvent = new CustomEvent("tab.show"), this.hideEvent = new CustomEvent("tab.hide")
    }
    n(6), document.addEventListener("DOMContentLoaded", function() {
        var t, e, n, r;
        p(), _()(), m(), t = document.querySelector("h1"), e = document.querySelector(".nhsuk-skip-link"), t && e && (e.addEventListener("click", function(e) {
                e.preventDefault(), t.setAttribute("tabIndex", "-1"), t.focus()
            }), t.addEventListener("blur", function(e) {
                e.preventDefault(), t.removeAttribute("tabIndex")
            })), n = document.querySelectorAll(".nhsuk-radios--conditional .nhsuk-radios__input"), r = function() {
                n.forEach(function(e) {
                    return y(e, "nhsuk-radios__conditional--hidden")
                })
            }, "onpageshow" in window ? window.addEventListener("pageshow", r) : window.addEventListener("DOMContentLoaded", r), r(), n.forEach(function(e) {
                e.addEventListener("change", r)
            }), b(),
            function(e) {
                var e = (0 < arguments.length && void 0 !== e ? e : {}).focusOnPageLoad,
                    e = void 0 === e || e,
                    t = document.querySelector(".nhsuk-error-summary");
                t && (e && t.focus(), t.addEventListener("click", g))
            }(), document.querySelectorAll(".nhsuk-card--clickable").forEach(function(e) {
                null !== e.querySelector("a") && e.addEventListener("click", function() {
                    e.querySelector("a").click()
                })
            }),
            function(e) {
                var e = 0 < arguments.length && void 0 !== e ? e : {},
                    t = e.namespace,
                    n = void 0 === t ? "nhsuk-tabs" : t,
                    t = e.responsive,
                    r = void 0 === t || t,
                    t = e.historyEnabled,
                    o = void 0 === t || t;
                document.querySelectorAll('[data-module="'.concat(n, '"]')).forEach(function(e) {
                    new E(e, n, r, o).init()
                })
            }({
                historyEnabled: !1,
                namespace: "nhsuk-gallery",
                responsive: !1
            })
    }), window.NHSUK_SETTINGS.USER_FEEDBACK_STORE_ENDPOINT && document.querySelector("#nhsuk-user-feedback-form") && (t()({
        formEndpoint: window.NHSUK_SETTINGS.USER_FEEDBACK_STORE_ENDPOINT
    }), document.querySelector("#nhsuk-user-feedback-form").addEventListener("onFeedback", function() {
        "function" == typeof hj && hj("trigger", "feedback_response")
    }))
}]);