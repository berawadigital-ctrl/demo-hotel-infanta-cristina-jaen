# Contenido de la demo Hotel Infanta Cristina (Jaén) (es/en/fr/de). Hechos de hotelinfantacristina.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones de clientes; sin precios.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hotel real.','en':' Images are illustrations and do not show the actual hotel.','fr':' Les images sont des illustrations et ne montrent pas l’hôtel réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hotel.'}
H={'es':['Doble / Twin y doble uso individual','Junior Suite y doble con salón'],'en':['Double / Twin and single-use double','Junior Suite and double with lounge'],'fr':['Double / Twin et double usage individuel','Junior Suite et double avec salon'],'de':['Doppel / Twin und Doppel zur Einzelnutzung','Junior Suite und Doppel mit Salon']}
RD={
'es':['Amplias, insonorizadas y con baño privado completo, wifi, minibar, caja de seguridad, escritorio y aire acondicionado o calefacción según temporada. Las dobles admiten cama supletoria para un niño.','Con salón completo y, en las Junior Suite, cama King o Queen Size, amplias terrazas, bañera de hidromasaje y café de cortesía.'],
'en':['Spacious, soundproofed rooms with a full private bathroom, wifi, minibar, safe, desk and air conditioning or heating depending on the season. Doubles can take an extra bed for a child.','With a full lounge and, in the Junior Suites, a King or Queen Size bed, large terraces, a hydromassage bath and complimentary coffee.'],
'fr':['Spacieuses, insonorisées, avec salle de bain privée complète, wifi, minibar, coffre-fort, bureau et climatisation ou chauffage selon la saison. Les doubles acceptent un lit d’appoint pour un enfant.','Avec salon complet et, dans les Junior Suites, lit King ou Queen Size, grandes terrasses, baignoire d’hydromassage et café de courtoisie.'],
'de':['Geräumig, schallisoliert, mit komplettem eigenem Bad, WLAN, Minibar, Safe, Schreibtisch sowie Klimaanlage oder Heizung je nach Jahreszeit. In den Doppelzimmern ist ein Zustellbett für ein Kind möglich.','Mit komplettem Salon und in den Junior Suiten mit King- oder Queen-Size-Bett, großen Terrassen, Whirlwanne und Kaffee als Aufmerksamkeit.']}
ART={
'hero':('hills',9851,['#1e2a22','#d9a35a','#f1d29a','#55704a','#41593a','#24321f']),
'intro':('arches',9852,['#eef0ea','#f8f8f4','#55704a','#41593a','#24321f']),
'r1':('columns',9861,['#ecefe8','#c99350','#55704a','#41593a','#24321f']),
'r2':('arches',9862,['#1e2a22','#e0aa64','#f4d7a6','#6a8560','#506a47','#2a3a25']),
'g1':('hills',9871,['#e8ece0','#f1e2c3','#d6a160','#93a382','#6d7f5c','#4a5a3c']),
'g2':('waves',9872,['#24321f','#edbd83','#f6deb5','#4f6a45','#3c5434','#22311d']),
'g3':('columns',9873,['#f0ece4','#f9f5ee','#9c6a36','#6a4a2a','#3a2a18']),
'g4':('skyline',9874,['#1e2a22','#e0aa64','#f4d7a6','#6a8560','#506a47','#2a3a25'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Infanta Cristina · Hotel en Jaén',see_rooms='Ver las habitaciones',hero_k='Jaén · Ctra. de Madrid 3',hero_t='Su hotel de referencia en el corazón de Jaén',hero_s='78 habitaciones, piscina al aire libre, gimnasio y restaurante propio.',
 intro_t='Comodidad en la capital del aceite de oliva',intro_p1='Un espacio cuidadosamente decorado y conocido por la calidad de sus servicios. Cada una de sus 78 habitaciones está pensada para la máxima comodidad de los huéspedes.',
 intro_p2='Recientemente ha sido reconocido con la «Q» de Calidad. En el Restaurante Az-Zait, en el propio hotel, el chef propone cocina tradicional de sabores andaluces, y cada mañana hay desayuno bufé.',
 stats=['78 habitaciones','Piscina al aire libre','Gimnasio','Recepción 24 horas'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Cinco tipos de habitación, todas insonorizadas y con baño privado completo.',
 svcs=['Restaurante Az-Zait','Desayuno bufé','Bar-cafetería','9 salones para eventos','Aparcamiento privado de pago','Carga de vehículos eléctricos'],
 around_s='Para descubrir la Catedral de la Asunción, los Baños árabes y el Palacio de Villardompardo, el Castillo de Santa Catalina y el Museo de Arte Íbero.',
 loc_p='Ctra. de Madrid 3 · 23009 Jaén.',
 chips=['¿Qué habitaciones tenéis?','¿Hay piscina?','¿Tenéis aparcamiento?','¿Cómo reservo?']),
'en':dict(title='Hotel Infanta Cristina · Hotel in Jaén',see_rooms='See the rooms',hero_k='Jaén · Ctra. de Madrid 3',hero_t='Your hotel of choice in the heart of Jaén',hero_s='78 rooms, an outdoor pool, a gym and its own restaurant.',
 intro_t='Comfort in the olive oil capital',intro_p1='A carefully decorated space known for the quality of its services. Each of its 78 rooms is designed for the utmost comfort of guests.',
 intro_p2='It was recently awarded the «Q» for Quality. At the Az-Zait Restaurant, inside the hotel, the chef offers traditional cooking with Andalusian flavours, and there is a breakfast buffet every morning.',
 stats=['78 rooms','Outdoor pool','Gym','24-hour reception'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Five room types, all soundproofed and with a full private bathroom.',
 svcs=['Az-Zait Restaurant','Breakfast buffet','Bar-café','9 event rooms','Private paid parking','Electric vehicle charging'],
 around_s='To discover the Cathedral of the Assumption, the Arab Baths and Villardompardo Palace, Santa Catalina Castle and the Museum of Iberian Art.',
 loc_p='Ctra. de Madrid 3 · 23009 Jaén.',
 chips=['Which rooms do you have?','Is there a pool?','Is there parking?','How do I book?']),
'fr':dict(title='Hotel Infanta Cristina · Hôtel à Jaén',see_rooms='Voir les chambres',hero_k='Jaén · Ctra. de Madrid 3',hero_t='Votre hôtel de référence au cœur de Jaén',hero_s='78 chambres, piscine extérieure, salle de sport et restaurant.',
 intro_t='Le confort dans la capitale de l’huile d’olive',intro_p1='Un lieu soigneusement décoré, connu pour la qualité de ses services. Chacune de ses 78 chambres est pensée pour le plus grand confort des clients.',
 intro_p2='Il a récemment reçu le label « Q » de Qualité. Au restaurant Az-Zait, dans l’hôtel, le chef propose une cuisine traditionnelle aux saveurs andalouses, et un petit-déjeuner buffet est servi chaque matin.',
 stats=['78 chambres','Piscine extérieure','Salle de sport','Réception 24 h/24'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Cinq types de chambres, toutes insonorisées avec salle de bain privée complète.',
 svcs=['Restaurant Az-Zait','Petit-déjeuner buffet','Bar-cafétéria','9 salons pour événements','Parking privé payant','Recharge de véhicules électriques'],
 around_s='Pour découvrir la cathédrale de l’Assomption, les bains arabes et le palais de Villardompardo, le château de Santa Catalina et le musée d’Art ibère.',
 loc_p='Ctra. de Madrid 3 · 23009 Jaén.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il une piscine ?','Avez-vous un parking ?','Comment réserver ?']),
'de':dict(title='Hotel Infanta Cristina · Hotel in Jaén',see_rooms='Zimmer ansehen',hero_k='Jaén · Ctra. de Madrid 3',hero_t='Ihr Hotel im Herzen von Jaén',hero_s='78 Zimmer, Außenpool, Fitnessraum und eigenes Restaurant.',
 intro_t='Komfort in der Hauptstadt des Olivenöls',intro_p1='Ein sorgfältig eingerichtetes Haus, bekannt für die Qualität seiner Leistungen. Jedes seiner 78 Zimmer ist auf den größten Komfort der Gäste ausgelegt.',
 intro_p2='Es wurde kürzlich mit dem „Q“ für Qualität ausgezeichnet. Im Restaurant Az-Zait im Hotel bietet der Küchenchef traditionelle Küche mit andalusischen Aromen, und jeden Morgen gibt es ein Frühstücksbuffet.',
 stats=['78 Zimmer','Außenpool','Fitnessraum','24-Stunden-Rezeption'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Fünf Zimmertypen, alle schallisoliert und mit komplettem eigenem Bad.',
 svcs=['Restaurant Az-Zait','Frühstücksbuffet','Bar-Cafeteria','9 Veranstaltungsräume','Kostenpflichtiger Privatparkplatz','Ladestation für E-Autos'],
 around_s='Zum Entdecken der Kathedrale Mariä Himmelfahrt, der Arabischen Bäder und des Palastes Villardompardo, der Burg Santa Catalina und des Museums für iberische Kunst.',
 loc_p='Ctra. de Madrid 3 · 23009 Jaén.',
 chips=['Welche Zimmer gibt es?','Gibt es einen Pool?','Gibt es Parkplätze?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RES='https://www.hotelinfantacristina.com/reservar.html';REN='https://www.hotelinfantacristina.com/EN/booking.html'
BOOK=dict(mode='engine',url=dict(es=RES,en=REN,fr=REN,de=REN))
D=dict(name='Hotel Infanta Cristina',ac='#1e2a22',ac2='#55704a',ac2_a11y='#41593a',book=BOOK,around=['Catedral de Jaén','Castillo de Santa Catalina'],foot=FOOT,
 address='Ctra. de Madrid 3 · 23009 Jaén',phones=['+34 953 263040'],emails=['reservas@hotelinfantacristina.com'],maps='Hotel Infanta Cristina, Carretera de Madrid 3, 23009 Jaén',t=T)
META=dict(repo='demo-hotel-infanta-cristina-jaen',name='Hotel Infanta Cristina',legal_name='HIJOS JUAN DELGADO MARTÍNEZ S.L. (aviso legal de su web)',registry_ids=['B23310287'],
 url='https://www.hotelinfantacristina.com/',domain='hotelinfantacristina.com',municipality='Jaén',province='Jaén',sector='hotel urbano de 78 habitaciones en Jaén',
 read_at='2026-10-30T10:52:00+01:00',created_at='2026-10-30T10:52:00+01:00',built_at='2026-10-30T11:10:00+01:00',audit_date='2026-10-30T10:50:44+01:00',
 rating=dict(value=4.2,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Hotel+Infanta+Cristina/@37.7813349,-3.7838338,17z/data=!4m9!3m8!1s0xd6dd7a82274df0b:0xdb130defd29e77e7!5m2!4m1!1i2!8m2!3d37.7813349!4d-3.7838338!16s%2Fg%2F1tqp_lpl'),
 book=dict(mode='engine',url=RES,note='motor de reservas real de su web (página reservar.html con el buscador Keytel/Synergy; versión inglesa EN/booking.html), HTTP 200 comprobado el 30/10/2026; su web solo está en español e inglés: fr y de usan la versión inglesa.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Hay piscina?','K02'),('¿Tenéis aparcamiento?','K03'),('¿Hay gimnasio?','K04'),('¿Tenéis restaurante?','K05'),('¿Hay desayuno?','K06'),('¿Cómo reservo?','K07'),('¿Podéis confirmarme disponibilidad para mañana?','K07'),('¿Dónde está el hotel?','K08'),('¿Cuál es el teléfono?','K09'),('¿Tenéis salones para eventos?','K10'),('¿Puedo cargar mi coche eléctrico?','K11'),('¿Cuánto cuesta la noche?',None),('¿Admitís mascotas?',None)],
'en':[('Which rooms do you have?','K01'),('Is there a pool?','K02'),('Is there parking?','K03'),('Is there a gym?','K04'),('Do you have a restaurant?','K05'),('Is breakfast available?','K06'),('How do I book?','K07'),('Can you confirm availability for tomorrow?','K07'),('Where is the hotel?','K08'),('What is the phone number?','K09'),('Do you have event rooms?','K10'),('Can I charge my electric car?','K11'),('How much is a night?',None),('Do you accept pets?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Y a-t-il une piscine ?','K02'),('Avez-vous un parking ?','K03'),('Y a-t-il une salle de sport ?','K04'),('Avez-vous un restaurant ?','K05'),('Y a-t-il un petit-déjeuner ?','K06'),('Comment réserver ?','K07'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K07'),('Où se trouve l’hôtel ?','K08'),('Quel est le numéro de téléphone ?','K09'),('Avez-vous des salons pour événements ?','K10'),('Puis-je recharger ma voiture électrique ?','K11'),('Combien coûte la nuit ?',None),('Acceptez-vous les animaux ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Gibt es einen Pool?','K02'),('Gibt es Parkplätze?','K03'),('Gibt es einen Fitnessraum?','K04'),('Haben Sie ein Restaurant?','K05'),('Gibt es Frühstück?','K06'),('Wie kann ich buchen?','K07'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K07'),('Wo liegt das Hotel?','K08'),('Wie lautet die Telefonnummer?','K09'),('Haben Sie Veranstaltungsräume?','K10'),('Kann ich mein Elektroauto laden?','K11'),('Was kostet eine Nacht?',None),('Sind Haustiere erlaubt?',None)]}
