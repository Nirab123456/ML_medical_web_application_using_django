(() => {
    var n = {
            719: (n, t, e) => {
                "use strict";
                e.d(t, {
                    Z: () => o
                });
                const o = "https://www.nhs.uk/nhs-app/account/"
            },
            687: (n, t, e) => {
                "use strict";
                e.d(t, {
                    Z: () => a
                });
                var o = e(81),
                    c = e.n(o),
                    i = e(645),
                    r = e.n(i)()(c());
                r.push([n.id, ".nhsuk-account__login{float:right;margin-left:1em;margin-right:-16px;position:relative;z-index:2}.nhsuk-account__login--icon{fill:#fff;height:1.6em;margin-left:.6em;position:relative;top:.4em;width:1.6em}.nhsuk-account__login--link,.nhsuk-account__login--link:visited,.nhsuk-account__login--link:hover{color:#fff;padding:1em}.nhsuk-account__login--link:focus .nhsuk-account__login--icon{fill:#212b32}@media(min-width: 40.0625em){.nhsuk-account__login{margin-right:-8px}.nhsuk-account__login--link,.nhsuk-account__login--link:hover{margin-right:.6em;padding:.6em}}", ""]);
                const a = r
            },
            645: n => {
                "use strict";
                n.exports = function(n) {
                    var t = [];
                    return t.toString = function() {
                        return this.map((function(t) {
                            var e = "",
                                o = void 0 !== t[5];
                            return t[4] && (e += "@supports (".concat(t[4], ") {")), t[2] && (e += "@media ".concat(t[2], " {")), o && (e += "@layer".concat(t[5].length > 0 ? " ".concat(t[5]) : "", " {")), e += n(t), o && (e += "}"), t[2] && (e += "}"), t[4] && (e += "}"), e
                        })).join("")
                    }, t.i = function(n, e, o, c, i) {
                        "string" == typeof n && (n = [
                            [null, n, void 0]
                        ]);
                        var r = {};
                        if (o)
                            for (var a = 0; a < this.length; a++) {
                                var s = this[a][0];
                                null != s && (r[s] = !0)
                            }
                        for (var u = 0; u < n.length; u++) {
                            var l = [].concat(n[u]);
                            o && r[l[0]] || (void 0 !== i && (void 0 === l[5] || (l[1] = "@layer".concat(l[5].length > 0 ? " ".concat(l[5]) : "", " {").concat(l[1], "}")), l[5] = i), e && (l[2] ? (l[1] = "@media ".concat(l[2], " {").concat(l[1], "}"), l[2] = e) : l[2] = e), c && (l[4] ? (l[1] = "@supports (".concat(l[4], ") {").concat(l[1], "}"), l[4] = c) : l[4] = "".concat(c)), t.push(l))
                        }
                    }, t
                }
            },
            81: n => {
                "use strict";
                n.exports = function(n) {
                    return n[1]
                }
            },
            419: (n, t, e) => {
                n.exports = '<div class="nhsuk-account__login">\n  <a class="nhsuk-account__login--link" href="' + e(719).Z + '">\n    My account<svg class="nhsuk-account__login--icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" height="26" width="26">\n      <path d="M16,18.2c-3.1,0-5.7-2.5-5.7-5.7s2.5-5.7,5.7-5.7c3.1,0,5.7,2.5,5.7,5.7 C21.7,15.7,19.1,18.2,16,18.2"/>\n      <path d="M16,0C7.2,0,0,7.2,0,16s7.2,16,16,16s16-7.2,16-16C32,7.2,24.8,0,16,0 M24.1,27.5V26 c0-3.5-2.5-6.3-5.7-6.3h-4.8C10.5,19.6,8,22.5,8,26v1.6C1.6,23.1,0,14.3,4.5,8S17.7,0,24,4.5S32,17.7,27.5,24 C26.6,25.4,25.4,26.6,24.1,27.5"/>\n    </svg></a>\n</div>\n'
            }
        },
        t = {};

    function e(o) {
        var c = t[o];
        if (void 0 !== c) return c.exports;
        var i = t[o] = {
            id: o,
            exports: {}
        };
        return n[o](i, i.exports, e), i.exports
    }
    e.n = n => {
        var t = n && n.__esModule ? () => n.default : () => n;
        return e.d(t, {
            a: t
        }), t
    }, e.d = (n, t) => {
        for (var o in t) e.o(t, o) && !e.o(n, o) && Object.defineProperty(n, o, {
            enumerable: !0,
            get: t[o]
        })
    }, e.o = (n, t) => Object.prototype.hasOwnProperty.call(n, t), (() => {
        "use strict";
        var n = e(419),
            t = e.n(n),
            o = e(687);
        const c = function() {
            var n = document.getElementById("content-header"),
                t = document.querySelector(".nhsuk-account__login"),
                e = document.querySelector(".nhsuk-header__search");
            n && t && e && (document.body.clientWidth > 625 ? n.appendChild(t) : n.insertBefore(t, e))
        };
        document.addEventListener("DOMContentLoaded", (function() {
            var n = document.getElementById("content-header");
            n && (n.insertAdjacentHTML("afterbegin", "<style>".concat(o.Z.toString(), "</style>")), n.insertAdjacentHTML("afterbegin", t()), c(), window.addEventListener("resize", c))
        }))
    })()
})();