load("@npm//@bazel/jasmine:index.bzl", "jasmine_node_test")

filegroup(
    name = "node_calculator",
    srcs = ["calculator.js"],
    visibility = ["//projects/node_web:__pkg__"]
)

# bazel query @npm//... | grep jasmine
jasmine_node_test(
    name = "caclulator_test",
    srcs = ["calculator.spec.js"],
    data = [":node_calculator"],
)