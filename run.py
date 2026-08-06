from app import create_app

app = create_app()

print("\n========== ROUTES ==========")
for rule in app.url_map.iter_rules():
    print(f"{rule.endpoint:35} -> {rule}")
print("============================\n")
print("\n===== REGISTERED ROUTES =====")
for rule in app.url_map.iter_rules():
    print(rule)
print("=============================\n")


if __name__ == "__main__":
    app.run(debug=True)