from functools import reduce

test_results = [
    {"name": "test_login", "module": "auth", "duration_ms": 1200, "status": "pass"},
    {"name": "test_register", "module": "auth", "duration_ms": 2100, "status": "pass"},
    {"name": "test_logout", "module": "auth", "duration_ms": 300, "status": "pass"},
    {"name": "test_search", "module": "search", "duration_ms": 850, "status": "fail"},
    {"name": "test_filter", "module": "search", "duration_ms": 1800, "status": "fail"},
    {"name": "test_sort", "module": "search", "duration_ms": 670, "status": "pass"},
    {"name": "test_add_cart", "module": "checkout", "duration_ms": 2300, "status": "fail"},
    {"name": "test_payment", "module": "checkout", "duration_ms": 3100, "status": "pass"},
    {"name": "test_confirm", "module": "checkout", "duration_ms": 1900, "status": "pass"},
    {"name": "test_view_profile", "module": "profile", "duration_ms": 380, "status": "pass"},
    {"name": "test_edit_profile", "module": "profile", "duration_ms": 540, "status": "pass"},
    {"name": "test_settings", "module": "profile", "duration_ms": 420, "status": "fail"},
]

sorted_by_duration = sorted(
    test_results,
    key=lambda test: test["duration_ms"]
)

sort_by_module_then_test = sorted(
    test_results,
    key=lambda test: (test["module"], test["duration_ms"]) 
)

sorted_by_status_then_name = sorted(
    test_results,
    key=lambda test: (
        0 if test["status"] == "fail" else 1,
        test["name"]
    )
)

test_names = list(map(
    lambda test: test["name"],
    test_results
))

test_failures = list(filter(
    lambda test: test["status"] == 'fail',
    test_results
))

slow_test = list(filter(
    lambda test: test['duration_ms'] > 1500,
    test_results
))

summary_of_test = list()


