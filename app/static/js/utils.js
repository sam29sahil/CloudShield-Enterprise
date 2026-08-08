/*
============================================================

CloudShield Enterprise
Core Utilities

File:
static/js/utils.js

============================================================
*/

"use strict";

/* ==========================================================
   CLOUDSHIELD CORE
========================================================== */

const CloudShield = (() => {

    /* ======================================================
       CONFIGURATION
    ====================================================== */

    const Config = {

        apiBase: "/",

        debug: true,

        animationSpeed: 300,

        toastDuration: 4000,

        loadingDelay: 200,

        theme: "dark"

    };

    /* ======================================================
       DOM HELPERS
    ====================================================== */

    const DOM = {

        id(id){

            return document.getElementById(id);

        },

        one(selector,parent=document){

            return parent.querySelector(selector);

        },

        all(selector,parent=document){

            return [...parent.querySelectorAll(selector)];

        },

        create(tag){

            return document.createElement(tag);

        },

        remove(element){

            if(element){

                element.remove();

            }

        },

        empty(element){

            if(element){

                element.innerHTML="";

            }

        },

        append(parent,child){

            if(parent && child){

                parent.appendChild(child);

            }

        },

        prepend(parent,child){

            if(parent && child){

                parent.prepend(child);

            }

        },

        html(element,html){

            if(!element) return;

            element.innerHTML=html;

        },

        text(element,text){

            if(!element) return;

            element.textContent=text;

        }

    };

    /* ======================================================
       CLASS HELPERS
    ====================================================== */

    const Class = {

        add(element,name){

            if(element){

                element.classList.add(name);

            }

        },

        remove(element,name){

            if(element){

                element.classList.remove(name);

            }

        },

        toggle(element,name){

            if(element){

                element.classList.toggle(name);

            }

        },

        contains(element,name){

            if(!element) return false;

            return element.classList.contains(name);

        }

    };

    /* ======================================================
       ATTRIBUTE HELPERS
    ====================================================== */

    const Attribute = {

        get(element,name){

            if(!element) return null;

            return element.getAttribute(name);

        },

        set(element,name,value){

            if(element){

                element.setAttribute(name,value);

            }

        },

        remove(element,name){

            if(element){

                element.removeAttribute(name);

            }

        }

    };

    /* ======================================================
       EVENT HELPERS
    ====================================================== */

    const Events = {

        on(element,event,callback){

            if(element){

                element.addEventListener(event,callback);

            }

        },

        off(element,event,callback){

            if(element){

                element.removeEventListener(event,callback);

            }

        },

        once(element,event,callback){

            if(element){

                element.addEventListener(event,callback,{
                    once:true
                });

            }

        },

        ready(callback){

            if(document.readyState==="loading"){

                document.addEventListener(
                    "DOMContentLoaded",
                    callback
                );

            }else{

                callback();

            }

        }

    };

    /* ======================================================
       VISIBILITY
    ====================================================== */

    const Visibility = {

        show(element){

            if(element){

                element.style.display="";

            }

        },

        hide(element){

            if(element){

                element.style.display="none";

            }

        },

        toggle(element){

            if(!element) return;

            element.style.display =
                element.style.display==="none"
                ? ""
                : "none";

        }

    };

    /* ======================================================
       RETURN
    ====================================================== */

    return {

        Config,

        DOM,

        Class,

        Attribute,

        Events,

        Visibility

    };

})();
/* ==========================================================
   API WRAPPER
========================================================== */

const API = {

    async request(url, options = {}) {

        const config = {

            method: options.method || "GET",

            headers: {
                "Content-Type": "application/json",
                ...(options.headers || {})
            },

            body: options.body
                ? JSON.stringify(options.body)
                : null

        };

        try {

            const response = await fetch(url, config);

            const data = await response.json();

            return {

                success: response.ok,

                status: response.status,

                data

            };

        } catch (error) {

            Logger.error(error);

            return {

                success: false,

                status: 500,

                data: error.message

            };

        }

    },

    get(url) {

        return this.request(url);

    },

    post(url, body) {

        return this.request(url, {

            method: "POST",

            body

        });

    },

    put(url, body) {

        return this.request(url, {

            method: "PUT",

            body

        });

    },

    delete(url) {

        return this.request(url, {

            method: "DELETE"

        });

    }

};

/* ==========================================================
   LOCAL STORAGE
========================================================== */

const Storage = {

    set(key, value) {

        localStorage.setItem(

            key,

            JSON.stringify(value)

        );

    },

    get(key, fallback = null) {

        const value = localStorage.getItem(key);

        if (!value) {

            return fallback;

        }

        try {

            return JSON.parse(value);

        }

        catch {

            return value;

        }

    },

    remove(key) {

        localStorage.removeItem(key);

    },

    clear() {

        localStorage.clear();

    }

};

/* ==========================================================
   SESSION STORAGE
========================================================== */

const Session = {

    set(key, value) {

        sessionStorage.setItem(

            key,

            JSON.stringify(value)

        );

    },

    get(key, fallback = null) {

        const value = sessionStorage.getItem(key);

        if (!value) {

            return fallback;

        }

        try {

            return JSON.parse(value);

        }

        catch {

            return value;

        }

    },

    remove(key) {

        sessionStorage.removeItem(key);

    },

    clear() {

        sessionStorage.clear();

    }

};

/* ==========================================================
   CLIPBOARD
========================================================== */

const Clipboard = {

    async copy(text) {

        try {

            await navigator.clipboard.writeText(text);

            return true;

        }

        catch {

            return false;

        }

    }

};

/* ==========================================================
   DOWNLOAD HELPERS
========================================================== */

const Download = {

    text(filename, text) {

        const blob = new Blob(

            [text],

            {

                type: "text/plain"

            }

        );

        this.blob(filename, blob);

    },

    json(filename, object) {

        const blob = new Blob(

            [

                JSON.stringify(

                    object,

                    null,

                    4

                )

            ],

            {

                type: "application/json"

            }

        );

        this.blob(filename, blob);

    },

    blob(filename, blob) {

        const url = URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        link.download = filename;

        document.body.appendChild(link);

        link.click();

        link.remove();

        URL.revokeObjectURL(url);

    }

};

/* ==========================================================
   URL HELPERS
========================================================== */

const URLHelper = {

    params() {

        return new URLSearchParams(

            window.location.search

        );

    },

    get(name) {

        return this.params().get(name);

    },

    has(name) {

        return this.params().has(name);

    }

};
/* ==========================================================
   API WRAPPER
========================================================== */

const API = {

    async request(url, options = {}) {

        const config = {

            method: options.method || "GET",

            headers: {
                "Content-Type": "application/json",
                ...(options.headers || {})
            },

            body: options.body
                ? JSON.stringify(options.body)
                : null

        };

        try {

            const response = await fetch(url, config);

            const data = await response.json();

            return {

                success: response.ok,

                status: response.status,

                data

            };

        } catch (error) {

            Logger.error(error);

            return {

                success: false,

                status: 500,

                data: error.message

            };

        }

    },

    get(url) {

        return this.request(url);

    },

    post(url, body) {

        return this.request(url, {

            method: "POST",

            body

        });

    },

    put(url, body) {

        return this.request(url, {

            method: "PUT",

            body

        });

    },

    delete(url) {

        return this.request(url, {

            method: "DELETE"

        });

    }

};

/* ==========================================================
   LOCAL STORAGE
========================================================== */

const Storage = {

    set(key, value) {

        localStorage.setItem(

            key,

            JSON.stringify(value)

        );

    },

    get(key, fallback = null) {

        const value = localStorage.getItem(key);

        if (!value) {

            return fallback;

        }

        try {

            return JSON.parse(value);

        }

        catch {

            return value;

        }

    },

    remove(key) {

        localStorage.removeItem(key);

    },

    clear() {

        localStorage.clear();

    }

};

/* ==========================================================
   SESSION STORAGE
========================================================== */

const Session = {

    set(key, value) {

        sessionStorage.setItem(

            key,

            JSON.stringify(value)

        );

    },

    get(key, fallback = null) {

        const value = sessionStorage.getItem(key);

        if (!value) {

            return fallback;

        }

        try {

            return JSON.parse(value);

        }

        catch {

            return value;

        }

    },

    remove(key) {

        sessionStorage.removeItem(key);

    },

    clear() {

        sessionStorage.clear();

    }

};

/* ==========================================================
   CLIPBOARD
========================================================== */

const Clipboard = {

    async copy(text) {

        try {

            await navigator.clipboard.writeText(text);

            return true;

        }

        catch {

            return false;

        }

    }

};

/* ==========================================================
   DOWNLOAD HELPERS
========================================================== */

const Download = {

    text(filename, text) {

        const blob = new Blob(

            [text],

            {

                type: "text/plain"

            }

        );

        this.blob(filename, blob);

    },

    json(filename, object) {

        const blob = new Blob(

            [

                JSON.stringify(

                    object,

                    null,

                    4

                )

            ],

            {

                type: "application/json"

            }

        );

        this.blob(filename, blob);

    },

    blob(filename, blob) {

        const url = URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        link.download = filename;

        document.body.appendChild(link);

        link.click();

        link.remove();

        URL.revokeObjectURL(url);

    }

};

/* ==========================================================
   URL HELPERS
========================================================== */

const URLHelper = {

    params() {

        return new URLSearchParams(

            window.location.search

        );

    },

    get(name) {

        return this.params().get(name);

    },

    has(name) {

        return this.params().has(name);

    }

};
/* ==========================================================
   TOAST NOTIFICATIONS
========================================================== */

const Toast = {

    container: null,

    init() {

        if (this.container) return;

        this.container = DOM.create("div");

        this.container.className = "toast-container";

        document.body.appendChild(this.container);

    },

    show(message, type = "info", duration = Config.toastDuration) {

        this.init();

        const toast = DOM.create("div");

        toast.className = `toast toast-${type}`;

        toast.innerHTML = `
            <div class="toast-content">
                <span>${message}</span>
            </div>
        `;

        this.container.appendChild(toast);

        requestAnimationFrame(() => {

            toast.classList.add("show");

        });

        setTimeout(() => {

            toast.classList.remove("show");

            setTimeout(() => {

                toast.remove();

            }, 300);

        }, duration);

    },

    success(message) {

        this.show(message, "success");

    },

    warning(message) {

        this.show(message, "warning");

    },

    error(message) {

        this.show(message, "danger");

    },

    info(message) {

        this.show(message, "info");

    }

};

/* ==========================================================
   LOADING OVERLAY
========================================================== */

const Loading = {

    overlay: null,

    show(text = "Loading...") {

        if (!this.overlay) {

            this.overlay = DOM.create("div");

            this.overlay.className = "loading-overlay";

            this.overlay.innerHTML = `
                <div class="loading-box">
                    <div class="spinner"></div>
                    <div class="loading-text">${text}</div>
                </div>
            `;

            document.body.appendChild(this.overlay);

        } else {

            this.overlay.querySelector(".loading-text").textContent = text;

        }

        this.overlay.style.display = "flex";

    },

    hide() {

        if (this.overlay) {

            this.overlay.style.display = "none";

        }

    }

};

/* ==========================================================
   MODAL MANAGER
========================================================== */

const Modal = {

    open(id) {

        const modal = DOM.id(id);

        if (!modal) return;

        Class.add(modal, "active");

        document.body.classList.add("modal-open");

    },

    close(id) {

        const modal = DOM.id(id);

        if (!modal) return;

        Class.remove(modal, "active");

        document.body.classList.remove("modal-open");

    },

    closeAll() {

        DOM.all(".modal.active").forEach(modal => {

            Class.remove(modal, "active");

        });

        document.body.classList.remove("modal-open");

    }

};

/* ==========================================================
   SIDEBAR MANAGER
========================================================== */

const Sidebar = {

    sidebar: null,

    init() {

        this.sidebar = DOM.one(".sidebar");

    },

    toggle() {

        if (!this.sidebar) {

            this.init();

        }

        if (this.sidebar) {

            Class.toggle(this.sidebar, "active");

        }

    },

    open() {

        if (!this.sidebar) {

            this.init();

        }

        if (this.sidebar) {

            Class.add(this.sidebar, "active");

        }

    },

    close() {

        if (!this.sidebar) {

            this.init();

        }

        if (this.sidebar) {

            Class.remove(this.sidebar, "active");

        }

    }

};

/* ==========================================================
   THEME MANAGER
========================================================== */

const Theme = {

    current() {

        return Storage.get("theme", Config.theme);

    },

    apply(theme) {

        document.documentElement.setAttribute(

            "data-theme",

            theme

        );

        Storage.set("theme", theme);

    },

    toggle() {

        const theme =

            this.current() === "dark"

            ? "light"

            : "dark";

        this.apply(theme);

    },

    init() {

        this.apply(this.current());

    }

};