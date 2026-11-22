#სავარჯიშო 1

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}", timeout=10)
    if response.status_code == 404:
        return None
    response.raise_for_status()      # 500 და სხვა შეცდომებზე exception
    return response.json()


for user_id in (1, 2, 999):
    user = get_user(user_id)
    if user is None:
        print(f"მომხმარებელი {user_id} ვერ მოიძებნა")
    else:
        print(f"{user['name']} | {user['email']} | {user['address']['city']}")



#სავარჯიშო 2

def crud_tour():
    # 1. CREATE
    r = requests.post(
        f"{BASE_URL}/posts",
        json={"title": "ახალი პოსტი", "body": "ტექსტი", "userId": 1},
        timeout=10,
    )
    new_id = r.json()["id"]
    print(f"CREATE: {r.status_code}, id={new_id}")

    # 2. READ
    r = requests.get(f"{BASE_URL}/posts/{new_id}", timeout=10)
    print(f"READ {new_id}: {r.status_code}")

    # 3. UPDATE (PUT) — სრული ობიექტი
    r = requests.put(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "სრულად შეცვლილი", "body": "ახალი ტექსტი", "userId": 1},
        timeout=10,
    )
    print(f"UPDATE (PUT): {r.status_code}, title={r.json()['title']}")

    # 4. UPDATE (PATCH) — მხოლოდ title
    r = requests.patch(
        f"{BASE_URL}/posts/1",
        json={"title": "ნაწილობრივ შეცვლილი"},
        timeout=10,
    )
    print(f"UPDATE (PATCH): {r.status_code}, title={r.json()['title']}")

    # 5. DELETE
    r = requests.delete(f"{BASE_URL}/posts/1", timeout=10)
    print(f"DELETE: {r.status_code}, {r.json()}")


crud_tour()
