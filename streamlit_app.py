
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="DeltaX Food | Order Online", page_icon="🍽️", layout="wide")

restaurants = [
    {"id":1,"name":"DeltaX Biryani House","cuisine":"Biryani, North Indian","rating":4.5,"time":"25-30 min","offer":"50% OFF up to ₹100","veg":False,"price_for_two":350,"image":"🍛","menu":[{"name":"Chicken Biryani","price":199,"veg":False},{"name":"Veg Biryani","price":149,"veg":True},{"name":"Paneer Tikka","price":179,"veg":True},{"name":"Raita","price":39,"veg":True}]},
    {"id":2,"name":"Pizza Planet DX","cuisine":"Pizza, Fast Food","rating":4.3,"time":"20-25 min","offer":"Buy 1 Get 1","veg":True,"price_for_two":450,"image":"🍕","menu":[{"name":"Margherita Pizza","price":199,"veg":True},{"name":"Farmhouse Pizza","price":279,"veg":True},{"name":"Garlic Bread","price":119,"veg":True},{"name":"Cold Drink","price":59,"veg":True}]},
    {"id":3,"name":"Burger Junction","cuisine":"Burger, Snacks","rating":4.2,"time":"18-22 min","offer":"₹75 OFF","veg":False,"price_for_two":250,"image":"🍔","menu":[{"name":"Veg Cheese Burger","price":99,"veg":True},{"name":"Chicken Burger","price":139,"veg":False},{"name":"French Fries","price":89,"veg":True},{"name":"Chocolate Shake","price":129,"veg":True}]},
    {"id":4,"name":"South Express","cuisine":"South Indian, Breakfast","rating":4.6,"time":"15-20 min","offer":"Free delivery","veg":True,"price_for_two":220,"image":"🥘","menu":[{"name":"Masala Dosa","price":109,"veg":True},{"name":"Idli Sambar","price":79,"veg":True},{"name":"Vada Sambar","price":89,"veg":True},{"name":"Filter Coffee","price":49,"veg":True}]},
    {"id":5,"name":"Chinese Wok DX","cuisine":"Chinese, Momos","rating":4.1,"time":"30-35 min","offer":"20% OFF","veg":False,"price_for_two":300,"image":"🥡","menu":[{"name":"Veg Hakka Noodles","price":139,"veg":True},{"name":"Chicken Fried Rice","price":169,"veg":False},{"name":"Veg Momos","price":99,"veg":True},{"name":"Chilli Chicken","price":199,"veg":False}]},
    {"id":6,"name":"Sweet Treats","cuisine":"Desserts, Ice Cream","rating":4.4,"time":"20-30 min","offer":"Flat ₹50 OFF","veg":True,"price_for_two":280,"image":"🍰","menu":[{"name":"Chocolate Cake","price":149,"veg":True},{"name":"Gulab Jamun","price":99,"veg":True},{"name":"Vanilla Ice Cream","price":89,"veg":True},{"name":"Brownie","price":129,"veg":True}]},
]

if "cart" not in st.session_state:
    st.session_state.cart=[]
if "selected_restaurant" not in st.session_state:
    st.session_state.selected_restaurant=None

st.markdown("""
<style>
.stApp{background:linear-gradient(180deg,#fff7ed 0%,#fff 36%,#f8fafc 100%)}
.hero{background:linear-gradient(135deg,#ff5a1f,#ff8a00);border-radius:28px;padding:38px;color:white;box-shadow:0 20px 50px rgba(255,90,31,.25);margin-bottom:24px}.hero h1{font-size:54px;margin:0;letter-spacing:-1px}.hero p{font-size:20px;opacity:.95}.brand-pill{display:inline-block;background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.35);padding:8px 16px;border-radius:999px;font-weight:700;margin-bottom:14px}.card{background:white;border:1px solid #f1f5f9;border-radius:24px;padding:22px;box-shadow:0 12px 30px rgba(15,23,42,.08);margin-bottom:18px}.restaurant-title{font-size:22px;font-weight:800;color:#111827}.restaurant-img{font-size:54px;text-align:center;background:#fff7ed;border-radius:18px;padding:18px}.offer{display:inline-block;background:#ecfdf5;color:#059669;padding:6px 12px;border-radius:999px;font-weight:800;font-size:13px}.meta{color:#4b5563;font-size:14px}.cart-box{background:#111827;color:white;border-radius:24px;padding:22px;box-shadow:0 12px 30px rgba(15,23,42,.18)}.cart-item{border-bottom:1px solid rgba(255,255,255,.12);padding:10px 0}.total{font-size:24px;font-weight:900;color:#22c55e}.small-muted{color:#94a3b8;font-size:13px}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero"><span class="brand-pill">🍽️ DeltaX Food Delivery</span><h1>Order Food Online Near You</h1><p>Search restaurants, explore menus, add items to cart, and place a demo order in seconds.</p></div>
""", unsafe_allow_html=True)

left, mid, right = st.columns([2,2,1])
with left:
    location=st.text_input("📍 Delivery location", placeholder="Enter your area, city or pincode")
with mid:
    search=st.text_input("🔍 Search restaurant or food", placeholder="Biryani, Pizza, Dosa, Burger...")
with right:
    veg_only=st.toggle("Veg only")
sort_by=st.radio("Sort by", ["Recommended","Rating","Fast Delivery","Low Price"], horizontal=True)

filtered=restaurants.copy()
if search:
    s=search.lower()
    filtered=[r for r in filtered if s in r["name"].lower() or s in r["cuisine"].lower() or any(s in item["name"].lower() for item in r["menu"])]
if veg_only:
    filtered=[r for r in filtered if r["veg"]]
if sort_by=="Rating": filtered=sorted(filtered,key=lambda r:r["rating"],reverse=True)
elif sort_by=="Fast Delivery": filtered=sorted(filtered,key=lambda r:int(r["time"].split("-")[0]))
elif sort_by=="Low Price": filtered=sorted(filtered,key=lambda r:r["price_for_two"])

main, cart_col=st.columns([2.2,1])
with main:
    st.subheader("Popular restaurants near you")
    if not filtered:
        st.warning("No restaurants found. Try another search.")
    else:
        cols=st.columns(2)
        for index,r in enumerate(filtered):
            with cols[index%2]:
                st.markdown(f"""<div class="card"><div class="restaurant-img">{r['image']}</div><div class="restaurant-title">{r['name']}</div><div class="meta">{r['cuisine']}</div><div class="meta">⭐ {r['rating']} • {r['time']} • ₹{r['price_for_two']} for two</div><br><span class="offer">{r['offer']}</span></div>""", unsafe_allow_html=True)
                if st.button("View Menu", key=f"view_{r['id']}", use_container_width=True):
                    st.session_state.selected_restaurant=r["id"]
    selected=next((r for r in restaurants if r["id"]==st.session_state.selected_restaurant), None)
    if selected:
        st.markdown("---")
        st.subheader(f"Menu — {selected['name']}")
        for item in selected["menu"]:
            c1,c2,c3=st.columns([3,1,1])
            with c1:
                veg_label="🟢 Veg" if item["veg"] else "🔴 Non-Veg"
                st.markdown(f"**{item['name']}**  \n{veg_label}")
            with c2:
                st.markdown(f"**₹{item['price']}**")
            with c3:
                if st.button("Add", key=f"add_{selected['id']}_{item['name']}"):
                    st.session_state.cart.append({"restaurant":selected["name"],"name":item["name"],"price":item["price"]})
                    st.success(f"Added {item['name']}")

with cart_col:
    st.markdown('<div class="cart-box">', unsafe_allow_html=True)
    st.markdown("### 🛒 Your Cart")
    if not st.session_state.cart:
        st.markdown('<p class="small-muted">Your cart is empty. Add items from any restaurant.</p>', unsafe_allow_html=True)
    else:
        subtotal=sum(i["price"] for i in st.session_state.cart)
        delivery_fee=29
        platform_fee=5
        total=subtotal+delivery_fee+platform_fee
        for idx,item in enumerate(st.session_state.cart):
            st.markdown(f"""<div class="cart-item"><b>{item['name']}</b><br><span class="small-muted">{item['restaurant']}</span><br>₹{item['price']}</div>""", unsafe_allow_html=True)
            if st.button("Remove", key=f"remove_{idx}", use_container_width=True):
                st.session_state.cart.pop(idx)
                st.rerun()
        st.markdown(f"Subtotal: ₹{subtotal}")
        st.markdown(f"Delivery fee: ₹{delivery_fee}")
        st.markdown(f"Platform fee: ₹{platform_fee}")
        st.markdown(f'<div class="total">Total: ₹{total}</div>', unsafe_allow_html=True)
        name=st.text_input("Your name")
        phone=st.text_input("Mobile number")
        address=st.text_area("Delivery address", value=location if location else "")
        if st.button("Place Demo Order", use_container_width=True):
            if not name or not phone or not address:
                st.warning("Please enter name, phone, and address.")
            else:
                order_id="DX"+datetime.now().strftime("%H%M%S")
                st.success(f"Order placed successfully! Order ID: {order_id}")
                st.balloons()
        if st.button("Clear Cart", use_container_width=True):
            st.session_state.cart=[]
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2026 DeltaX Food. Demo food-ordering website. Payments and real restaurant orders are not enabled.")
