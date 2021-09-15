import streamlit as st
st.title(" @@!! RB UNIT CONVERTER !!@@ ")
st.image("unit-converter.jpg")
nav = st.sidebar.radio("navigation", ["home", "converter"])
if nav == "home":
    s, r = st.beta_columns(2)
    if s.button("HELP!!"):
        st.write("Go And Search on google!!!@")
    if r.button("TABLE!!"):
        st.image("table.jpg")

if nav == "converter":
    rs = st.sidebar.selectbox("select any unit", ("length", "weight", "time", "speed"))
if rs == "length":
    ln, cho, nxt = st.beta_columns(3)
    pu = ln.number_input("enter the amount", 1.0, 1000.0, step=1.0)
    en = cho.selectbox("present unit", ("mm", "cm", "m", "km", "ft.", "inch"))
    rb = nxt.selectbox("wanted unit", ("mm", "cm", "m", "km", "ft.", "inch"))
    if en == rb:
        st.write(pu)
    elif en == "mm" and rb == "cm":
        st.write(pu / 10.0)
    elif en == "mm" and rb == "m":
        st.write(pu / 1000.0)
    elif en == "mm" and rb == "km":
        st.write(pu / 1000000.0)
    elif en == "cm" and rb == "mm":
        st.write(pu * 10.0)
    elif en == "cm" and rb == "m":
        st.write(pu / 100.0)
    elif en == "cm" and rb == "km":
        st.write(pu / 100000.0)
    elif en == "cm" and rb == "ft.":
        st.write(pu / 30.48)
    elif en == "cm" and rb == "inch":
        st.write(pu / 2.54)
    elif en == "m" and rb == "mm":
        st.write(pu * 1000.0)
    elif en == "m" and rb == "cm":
        st.write(pu / 100.0)
    elif en == "m" and rb == "km":
        st.write(pu / 1000.0)
    elif en == "m" and rb == "ft.":
        st.write(pu * 3.281)
    elif en == "m" and rb == "inch":
        st.write(pu * 39.37)
    elif en == "inch" and rb == "mm":
        st.write(pu * 25.40)
    elif en == "inch" and rb == "cm":
        st.write(pu * 2.54)
    elif en == "inch" and rb == "m":
        st.write(pu / 39.37)
    elif en == "inch" and rb == "km":
        st.write(pu / 39370)
    elif en == "inch" and rb == "ft.":
        st.write(pu / 12)
    elif en == "ft." and rb == "mm":
        st.write(pu * 304.8)
    elif en == "ft." and rb == "cm":
        st.write(pu * 34.48)
    elif en == "ft." and rb == "m":
        st.write(pu / 3.281)
    elif en == "ft." and rb == "km":
        st.write(pu / 3281)
    elif en == "ft." and rb == "inch":
        st.write(pu * 12)
    elif en == "km" and rb == "mm":
        st.write(pu * 1000000)
    elif en == "km" and rb == "cm":
        st.write(pu * 100000)
    elif en == "km" and rb == "m":
        st.write(pu * 1000)
    elif en == "km" and rb == "inch":
        st.write(pu * 39370)
    elif en == "km" and rb == "ft.":
        st.write(pu * 3281)
if rs == "time":
    rt, sta, rsa = st.beta_columns(3)
    pq = rt.number_input("enter the value", 1.0, 10000.0, step=1.0)
    qw = sta.selectbox("present unit", ("sec", "min", "hour"))
    qt = rsa.selectbox("wanted unit", ("sec", "min", "hour"))
    if qw == qt:
        st.write(pq)
    elif qw == "sec" and qt == "min":
        st.write(pq / 60)
    elif qw == "sec" and qt == "hour":
        st.write(pq / 3600)
    elif qw == "min" and qt == "sec":
        st.write(pq * 60)
    elif qw == "min" and qt == "hour":
        st.write(pq / 60)
    elif qw == "hour" and qt == "min":
        st.write(pq * 60)
    elif qw == "hour" and qt == "sec":
        st.write(pq * 3600)
if st.button("@@THANK@@"):
    st.balloons()




























