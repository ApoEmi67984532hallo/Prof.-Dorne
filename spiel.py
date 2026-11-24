import streamlit as st

st.set_page_config(page_title="Flucht vor Prof. Drone", page_icon="cover.jpeg")

# Spielstand & Inventar im Gedächtnis der App speichern
if "schritt" not in st.session_state:
    st.session_state.schritt = "start"
if "inventar" not in st.session_state:
    st.session_state.inventar = []
if "zustand" not in st.session_state:
    st.session_state.zustand = []
if "name" not in st.session_state:
    st.session_state.name = ""

# Titel der App
st.title("🔦 Flucht vor Prof. Drone")

# Status-Leiste oben anzeigen, sobald man etwas hat
if st.session_state.inventar or st.session_state.zustand:
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.inventar:
            st.info("🎒 **Tasche:** " + ", ".join(st.session_state.inventar))
    with col2:
        if st.session_state.zustand:
            st.warning("❤️ **Zustand:** " + ", ".join(st.session_state.zustand))

st.divider()

# --- SCHRITT 1: START ---
if st.session_state.schritt == "start":
    st.image("cover.jpeg", use_container_width=True)
    st.subheader("Bist du bereit?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Ja", use_container_width=True):
            st.session_state.schritt = "intro"
            st.rerun()
    with col2:
        if st.button("❌ Nein", use_container_width=True):
            st.session_state.schritt = "sicher"
            st.rerun()

# --- ZWISCHENSCHRITT: WENN "NEIN" GEDRÜCKT WURDE ---
elif st.session_state.schritt == "sicher":
    st.subheader("Bist du dir sicher?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Doch, ich bin bereit!", use_container_width=True):
            st.session_state.schritt = "intro"
            st.rerun()
    with col2:
        if st.button("Ja, ich bin mir sicher!", use_container_width=True):
            st.session_state.schritt = "egal_start"
            st.rerun()

elif st.session_state.schritt == "egal_start":
    st.write("*Egal, lass uns starten!*")
    if st.button("Weiter ➡️"):
        st.session_state.schritt = "intro"
        st.rerun()

# --- SCHRITT 2: DIE GESCHICHTE BEGINNT ---
elif st.session_state.schritt == "intro":
    st.write("⏳ *loading...*")
    st.write(
        "Du wachst in einem fremden Raum auf, es ist dunkel. Als du dich umschaust, "
        "siehst du ein kleines, enges Fenster, wodurch nur ein einziger Lichtstrahl leuchtet. "
        "Vor dem Fenster ist ein enges Gitter. *'Da passt kein Mensch durch'*, denkst du dir. "
        "Nachdem du eine Weile nachdenkst, erschließt du dir, dass dies wahrscheinlich ein Keller ist. "
        "Nicht deiner."
    )
    st.write(
        "Rechts neben dir findest du eine Tasche. In der Tasche findest du einen Brief:"
    )
    st.info(
        "✉️ *'Willkommen in meinem Labor. Du und deine Freunde werdet mein nächstes Testobjekt sein. "
        "Ich habe bei allen meinen Versuchskaninchen jedoch eine Regel. Ihr habt 7 Tage zu entkommen. "
        "Lasst euch nicht erwischen, liebe Grüße, Prof. Drone.'*"
    )
    st.write("Du hebst die Tasche auf.")
    st.divider()
    st.write("**Du schaust dich um. Was möchtest du tun?**")

    if st.button("🪟 (A) Versuchen aus dem Fenster zu klettern", use_container_width=True):
        st.session_state.zustand.append("Wunde")
        st.session_state.schritt = "wahl_a"
        st.rerun()

    if st.button("🔍 (B) Den Raum erkunden", use_container_width=True):
        st.session_state.inventar.append("Taschenlampe")
        st.session_state.schritt = "wahl_b"
        st.rerun()

# --- SCHRITT 3A: FENSTER ---
elif st.session_state.schritt == "wahl_a":
    st.write(
        "Du reißt an dem Gitter, jedoch ohne Erfolg. Es bewegt sich nichts. "
        "Als du probierst, stärker zu ziehen, rutscht du ab und verletzt dich."
    )
    st.error("🩸 **Du hast jetzt eine Wunde**")
    if st.button("Weiter ➡️"):
        st.session_state.schritt = "name_fragen"
        st.rerun()

# --- SCHRITT 3B: RAUM ERKUNDEN ---
elif st.session_state.schritt == "wahl_b":
    st.write(
        "Du schaust dich um und tastest an einer Wand entlang. Du stößt gegen einen Schrank, "
        "wodurch eine Box runterfällt. Als du die Box öffnest, findest du eine Taschenlampe. "
        "Du hebst sie auf und tust sie in die Tasche."
    )
    st.success("🔦 **Du hast jetzt eine Taschenlampe**")
    if st.button("Weiter ➡️"):
        st.session_state.schritt = "name_fragen"
        st.rerun()

# --- SCHRITT 4: NAME ABFRAGEN ---
elif st.session_state.schritt == "name_fragen":
    st.write("Du überlegst, was dein Name ist...")
    eingabe = st.text_input("Was ist dein Name?")
    if st.button("Namen bestätigen"):
        if eingabe.strip() != "":
            st.session_state.name = eingabe
            st.session_state.schritt = "tag1_ende"
            st.rerun()
        else:
            st.warning("Bitte gib zuerst einen Namen ein!")

# --- SCHRITT 5: ENDE VON TAG 1 ---
elif st.session_state.schritt == "tag1_ende":
    st.write(f"Genau! Mein Name war **{st.session_state.name}**.")
    st.write("Es wird langsam dunkel, also entscheidest du dich ins Bett zu gehen.")
    st.divider()
    st.subheader("🌙 ~ TAG 1 IST VORBEI ~")

    if st.button("🔄 Spiel neu starten"):
        st.session_state.schritt = "start"
        st.session_state.inventar = []
        st.session_state.zustand = []
        st.session_state.name = ""
        st.rerun()
