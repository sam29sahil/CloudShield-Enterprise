"""
CloudShield Enterprise
<<<<<<< HEAD
Tool Registry
"""

# ==========================================================
# Tool Categories
=======
Enterprise Tool Registry
"""

from __future__ import annotations

from typing import Dict, List, Optional

# ==========================================================
# Category Loaders
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# ==========================================================

from app.security.tools.basic import get_all_tools as basic_tools
from app.security.tools.network import get_all_tools as network_tools
from app.security.tools.web import get_all_tools as web_tools
from app.security.tools.ssl import get_all_tools as ssl_tools
from app.security.tools.dns import get_all_tools as dns_tools
from app.security.tools.cloud import get_all_tools as cloud_tools
from app.security.tools.wireless import get_all_tools as wireless_tools

<<<<<<< HEAD
=======

# ==========================================================
# Category Registry
# ==========================================================

CATEGORY_LOADERS = {

    "basic": basic_tools,

    "network": network_tools,

    "web": web_tools,

    "ssl": ssl_tools,

    "dns": dns_tools,

    "cloud": cloud_tools,

    "wireless": wireless_tools,

}


# ==========================================================
# Registry Cache
# ==========================================================

_registry_cache = None

_metadata_cache = None


# ==========================================================
# Metadata Defaults
# ==========================================================

DEFAULT_MODES = [

    "quick",

    "standard",

    "deep",

    "enterprise"

]


DEFAULT_TIMEOUT = 300

DEFAULT_PRIORITY = 100


>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# ==========================================================
# Registry Loader
# ==========================================================

<<<<<<< HEAD

def load_registry():
    """
    Load every registered security tool.
    """

    registry = {}

    registry.update(basic_tools())
    registry.update(network_tools())
    registry.update(web_tools())
    registry.update(ssl_tools())
    registry.update(dns_tools())
    registry.update(cloud_tools())
    registry.update(wireless_tools())
=======
def load_registry(force_reload=False):
    """
    Load every available security tool.

    Returns

        {
            "tool_name": ToolInstance()
        }
    """

    global _registry_cache

    if _registry_cache is not None and not force_reload:

        return _registry_cache

    registry = {}

    for loader in CATEGORY_LOADERS.values():

        try:

            registry.update(loader())

        except Exception as e:

            print(

                f"[Registry] Failed loading "

                f"{loader.__name__}: {e}"

            )

    _registry_cache = registry
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    return registry


# ==========================================================
<<<<<<< HEAD
# Categories
# ==========================================================

CATEGORIES = {
    "basic": list(basic_tools().keys()),
    "network": list(network_tools().keys()),
    "web": list(web_tools().keys()),
    "ssl": list(ssl_tools().keys()),
    "dns": list(dns_tools().keys()),
    "cloud": list(cloud_tools().keys()),
    "wireless": list(wireless_tools().keys()),
}


def get_categories():
    """
    Return all registered categories.
    """

    return CATEGORIES


# ==========================================================
# Helper Functions
# ==========================================================
=======
# Metadata Loader
# ==========================================================

def load_metadata(force_reload=False):
    """
    Build metadata for every tool.

    Metadata comes from the tool itself if possible.

    Otherwise defaults are used.
    """

    global _metadata_cache

    if _metadata_cache is not None and not force_reload:

        return _metadata_cache

    metadata = {}

    registry = load_registry(force_reload)

    for name, tool in registry.items():

        try:

            if hasattr(tool, "metadata"):

                data = tool.metadata()

            else:

                data = {}

        except Exception:

            data = {}

        metadata[name] = {

            "name": data.get(

                "name",

                name

            ),

            "display_name": data.get(

                "display_name",

                name.title()

            ),

            "category": data.get(

                "category",

                infer_category(name)

            ),

            "description": data.get(

                "description",

                ""

            ),

            "enabled": data.get(

                "enabled",

                True

            ),

            "always": data.get(

                "always",

                False

            ),

            "priority": data.get(

                "priority",

                DEFAULT_PRIORITY

            ),

            "timeout": data.get(

                "timeout",

                DEFAULT_TIMEOUT

            ),

            "passive": data.get(

                "passive",

                False

            ),

            "requires_https": data.get(

                "requires_https",

                False

            ),

            "modes": data.get(

                "modes",

                DEFAULT_MODES

            )

        }

    _metadata_cache = metadata

    return metadata


# ==========================================================
# Category Detection
# ==========================================================

def infer_category(tool_name):
    """
    Infer category when a tool
    does not expose metadata().
    """

    tool_name = tool_name.lower()

    for category, loader in CATEGORY_LOADERS.items():

        try:

            if tool_name in loader():

                return category

        except Exception:

            continue

    return "unknown"


# ==========================================================
# Cache Helpers
# ==========================================================

def reload_registry():
    """
    Reload registry and metadata.
    """

    global _registry_cache

    global _metadata_cache

    _registry_cache = None

    _metadata_cache = None

    load_registry(True)

    load_metadata(True)
    
    # ==========================================================
# Category Helpers
# ==========================================================

def get_categories():
    """
    Return all available categories.
    """

    return sorted(CATEGORY_LOADERS.keys())
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


def get_tools(category):
    """
    Return all tools for a category.
    """

<<<<<<< HEAD
    return CATEGORIES.get(category.lower(), [])


def tool_exists(tool):
    """
    Check if a tool is registered.
    """

    return tool.lower() in load_registry()
=======
    loader = CATEGORY_LOADERS.get(category.lower())

    if loader is None:

        return {}

    try:

        return loader()

    except Exception:

        return {}


def get_tool_names(category):
    """
    Return tool names for UI.
    """

    return sorted(

        get_tools(category).keys()

    )


# ==========================================================
# Tool Lookup
# ==========================================================

def get_tool(name):
    """
    Return a tool instance.
    """

    if not name:

        return None

    return load_registry().get(

        name.lower()

    )


def tool_exists(name):
    """
    Check whether a tool exists.
    """

    if not name:

        return False

    return name.lower() in load_registry()


def get_metadata(name):
    """
    Return metadata for a tool.
    """

    return load_metadata().get(

        name.lower(),

        {}

    )


# ==========================================================
# Tool Filters
# ==========================================================

def get_enabled_tools():
    """
    Return enabled tools only.
    """

    registry = load_registry()

    metadata = load_metadata()

    enabled = {}

    for name, tool in registry.items():

        info = metadata.get(name, {})

        if info.get("enabled", True):

            enabled[name] = tool

    return enabled


def get_always_tools():
    """
    Return tools that always execute.
    """

    registry = load_registry()

    metadata = load_metadata()

    tools = []

    for name, tool in registry.items():

        info = metadata.get(name, {})

        if info.get("always", False):

            tools.append(tool)

    return tools


# ==========================================================
# Mode Filters
# ==========================================================

def get_tools_for_mode(category, mode):
    """
    Return tools for category + mode.
    """

    category = category.lower()

    mode = mode.lower()

    metadata = load_metadata()

    tools = []

    for name, tool in get_tools(category).items():

        info = metadata.get(name, {})

        if not info.get("enabled", True):

            continue

        if mode in info.get("modes", DEFAULT_MODES):

            tools.append(tool)

    return tools


# ==========================================================
# Priority Sorting
# ==========================================================

def get_sorted_tools(category, mode):
    """
    Return execution list ordered
    by priority.
    """

    metadata = load_metadata()

    tools = get_tools_for_mode(

        category,

        mode

    )

    return sorted(

        tools,

        key=lambda tool: metadata.get(

            tool.name,

            {}

        ).get(

            "priority",

            DEFAULT_PRIORITY

        )

    )

# ==========================================================
# Registry Statistics
# ==========================================================

def registry_summary():
    """
    Return registry summary.
    """

    registry = load_registry()

    metadata = load_metadata()

    summary = {

        "total_categories": len(CATEGORY_LOADERS),

        "total_tools": len(registry),

        "enabled_tools": 0,

        "disabled_tools": 0,

        "always_run": 0,

        "categories": {}

    }

    for category in CATEGORY_LOADERS:

        summary["categories"][category] = len(

            get_tools(category)

        )

    for info in metadata.values():

        if info.get("enabled", True):

            summary["enabled_tools"] += 1

        else:

            summary["disabled_tools"] += 1

        if info.get("always", False):

            summary["always_run"] += 1

    return summary


# ==========================================================
# Registry Validation
# ==========================================================

def validate_registry():
    """
    Validate registry integrity.
    """

    errors = []

    registry = load_registry()

    metadata = load_metadata()

    for name in registry:

        if name not in metadata:

            errors.append(

                f"{name} missing metadata."

            )

    return {

        "success": len(errors) == 0,

        "errors": errors

    }


# ==========================================================
# Utility Helpers
# ==========================================================

def registry_size():

    return len(load_registry())


def metadata_size():

    return len(load_metadata())


def registry_loaded():

    return _registry_cache is not None


def metadata_loaded():

    return _metadata_cache is not None


# ==========================================================
# Compatibility Helpers
# ==========================================================

def category_exists(category):

    return category.lower() in CATEGORY_LOADERS


def available_tools(category):

    return get_tool_names(category)


def available_categories():

    return get_categories()


# ==========================================================
# Export
# ==========================================================

__all__ = [

    "load_registry",

    "reload_registry",

    "load_metadata",

    "get_categories",

    "available_categories",

    "get_tools",

    "available_tools",

    "get_tool",

    "tool_exists",

    "get_tool_names",

    "get_metadata",

    "get_enabled_tools",

    "get_always_tools",

    "get_tools_for_mode",

    "get_sorted_tools",

    "registry_summary",

    "validate_registry",

    "registry_size",

    "metadata_size",

    "registry_loaded",

    "metadata_loaded",

    "category_exists"

]      
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
