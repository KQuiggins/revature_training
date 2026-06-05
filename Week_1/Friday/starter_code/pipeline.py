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

summary_of_test = list(map(
    lambda test: 
        f"{'✅' if test['status'] == 'pass' else '❌'}"
        f" {test['name']}"
        f" ({test['duration_ms']}ms)",
    test_results

))

unique_module_names = set(map(
    lambda test: test['module'],
    test_results
))

# total = reduce(lambda a, b: a + b, nums)
duration_of_all_test = reduce(
    lambda total, test: total + test['duration_ms'],
    test_results,
    0
)

sum_of_failure_times = reduce(
    lambda total, test: total + test['duration_ms'],
    filter(
        lambda test: test["status"] == "fail",
        test_results
    ),
    0
)

longest_test_name = reduce(
    lambda longest, current:
        current
        if len(current["name"]) > len(longest["name"])
        else longest,
    test_results
)

module_summary_dict = reduce(
    lambda acc, test: {
        **acc,
        test["module"]: acc.get(test["module"], 0) + 1
    },
    test_results,
    {}
)

endpoints = ["/login", "/search", "/checkout", "/profile"]
expected_codes = [200, 200, 201, 200]
actual_codes = [200, 500, 201, 403]

for endpoint, expected, actual in zip(
    endpoints,
    expected_codes,
    actual_codes
):
    status = "PASS" if expected == actual else "FAIL"
    print(
        f"{endpoint}: "
        f"expected {expected}, "
        f"got {actual} -> {status}"
    )

names, modules, duration, statuses = zip(*[
    (
        test["name"],
        test["module"],
        test["duration_ms"],
        test["status"]
    )
    for test in test_results
])

name_duration_map = dict(zip(names, duration))
print(name_duration_map)


