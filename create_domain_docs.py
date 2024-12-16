#Import Langchain
from langchain_core.documents import Document

#Create Agriculture Food Documents
document_1 = Document(
    page_content="Local farmers adopt sustainable practices to improve crop yield and soil health for future generations.",
    metadata={
        "Domain": "Agriculture and Food Industry",
        "Topic": "Farming",
        "Category": "Sustainability",
        "Published Date": "2023-10-03",
        "Source": "Agri News Today",
        "Author": "Olivia Wright",
        "Tags": ["Farming", "Sustainability"],
        "Keywords": ["sustainable farming", "crop yield"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=1
)

document_2 = Document(
    page_content="Technological innovations in precision agriculture are optimizing resource use and boosting efficiency.",
    metadata={
        "Domain": "Agriculture and Food Industry",
        "Topic": "Precision Agriculture",
        "Category": "Technology",
        "Published Date": "2023-09-29",
        "Source": "Tech in Ag Journal",
        "Author": "Mark Chen",
        "Tags": ["Technology", "Efficiency"],
        "Keywords": ["precision farming, resource optimization"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=2
)

document_3 = Document(
    page_content="Organic farming methods increase in popularity as consumer demand for organic food grows.",
    metadata={
        "Domain": "Agriculture and Food Industry",
        "Topic": "Organic Farming",
        "Category": "Consumer Trends",
        "Published Date": "2023-09-26",
        "Source": "Organic Farming Daily",
        "Author": "Samantha Price",
        "Tags": ["Organic", "Consumer Demand"],
        "Keywords": ["organic farming", "food trends"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=3
)

document_4 = Document(
    page_content="The rise of plant-based food products is transforming the traditional meat and dairy industries.",
    metadata={
        "Domain": "Agriculture and Food Industry",
        "Topic": "Plant-Based Foods",
        "Category": "Food Industry",
        "Published Date": "2023-10-01",
        "Source": "Food Trend Review",
        "Author": "Mike Long",
        "Tags": ["Plant-Based", "Food Innovation"],
        "Keywords": ["meat alternatives", "dairy substitutes"],
        "Language": "English",
        "Sentiment": "Optimistic"
    },
    id=4
)

document_5 = Document(
    page_content="Drought-resistant crop varieties are developed to sustain agricultural productivity amid climate challenges.",
    metadata={
        "Domain": "Agriculture and Food Industry",
        "Topic": "Crop Science",
        "Category": "Innovation",
        "Published Date": "2023-09-28",
        "Source": "Ag Science Digest",
        "Author": "Olivia Wright",
        "Tags": ["Crop Science", "Climate"],
        "Keywords": ["drought resistance", "agricultural innovation"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=5
)

document_6 = Document(
    page_content="Agroecology practices are promoting biodiversity and ecological sustainability in farming systems.",
    metadata={
        "Domain": "Agriculture and Food Industry",
        "Topic": "Agroecology",
        "Category": "Ecology",
        "Published Date": "2023-09-30",
        "Source": "Eco Farming Review",
        "Author": "Mark Chen",
        "Tags": ["Agroecology", "Biodiversity"],
        "Keywords": ["farming systems", "ecological sustainability"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=6
)

document_7 = Document(
    page_content="Vertical farming techniques are providing fresh food solutions in urban environments worldwide.",
    metadata={
        "Domain": "Agriculture and Food Industry",
        "Topic": "Vertical Farming",
        "Category": "Urban Agriculture",
        "Published Date": "2023-09-25",
        "Source": "Urban Agri News",
        "Author": "Samantha Price",
        "Tags": ["Vertical Farming", "Urban Solutions"],
        "Keywords": ["fresh food", "urban farming"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=7
)

document_8 = Document(
    page_content="The global food logistics industry is leveraging AI to enhance supply chain efficiency and reduce waste.",
    metadata={
        "Domain": "Agriculture and Food Industry",
        "Topic": "Food Logistics",
        "Category": "Technology",
        "Published Date": "2023-09-22",
        "Source": "Logistics and Food",
        "Author": "Mike Long",
        "Tags": ["Food Logistics", "AI"],
        "Keywords": ["supply chain", "efficiency"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=8
)

document_9 = Document(
    page_content="Consumer interest in local foods is driving farmers' markets and community-supported agriculture.",
    metadata={
        "Domain": "Agriculture and Food Industry",
        "Topic": "Local Foods",
        "Category": "Community",
        "Published Date": "2023-09-27",
        "Source": "Local Food News",
        "Author": "Olivia Wright",
        "Tags": ["Local Foods", "Community Markets"],
        "Keywords": ["farmers' markets", "local produce"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=9
)

document_10 = Document(
    page_content="Food safety protocols are becoming increasingly important in the prevention of foodborne illnesses.",
    metadata={
        "Domain": "Agriculture and Food Industry",
        "Topic": "Food Safety",
        "Category": "Health",
        "Published Date": "2023-09-24",
        "Source": "Food Safety Journal",
        "Author": "Samantha Price",
        "Tags": ["Food Safety", "Health"],
        "Keywords": ["safety protocols", "foodborne illnesses"],
        "Language": "English",
        "Sentiment": "Concerned"
    },
    id=10
)

agriculture_food_docs = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
]

#Create Travel Tourism Documents
document_1 = Document(
    page_content="Popular European cities are seeing a resurgence in tourism as international travel picks up.",
    metadata={
        "Domain": "Travel and Tourism",
        "Topic": "International Travel",
        "Category": "Tourism Trends",
        "Published Date": "2023-09-23",
        "Source": "Travel World News",
        "Author": "Sarah Cole",
        "Tags": ["Tourism", "Europe"],
        "Keywords": ["travel trends", "Europe"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=1
)

document_2 = Document(
    page_content="Eco-friendly travel destinations are gaining attention as travelers seek sustainable experiences.",
    metadata={
        "Domain": "Travel and Tourism",
        "Topic": "Eco-tourism",
        "Category": "Sustainability",
        "Published Date": "2023-09-29",
        "Source": "Green Travel Guide",
        "Author": "Brian Chen",
        "Tags": ["Eco-tourism", "Sustainability"],
        "Keywords": ["sustainable travel", "eco-friendly destinations"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=2
)

document_3 = Document(
    page_content="Virtual reality tours offer immersive experiences of distant locations and historical sites.",
    metadata={
        "Domain": "Travel and Tourism",
        "Topic": "Virtual Tourism",
        "Category": "Technology",
        "Published Date": "2023-10-01",
        "Source": "Travel Tech Innovator",
        "Author": "Mia Kwan",
        "Tags": ["VR Tourism", "Innovation"],
        "Keywords": ["virtual reality", "tourism"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=3
)

document_4 = Document(
    page_content="Airlines are increasing flights to popular destinations as travel demand surges post-pandemic.",
    metadata={
        "Domain": "Travel and Tourism",
        "Topic": "Air Travel",
        "Category": "Demand",
        "Published Date": "2023-09-26",
        "Source": "Aviation News Today",
        "Author": "Sarah Cole",
        "Tags": ["Airlines", "Travel Demand"],
        "Keywords": ["flights", "post-pandemic travel"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=4
)

document_5 = Document(
    page_content="Travel bloggers share their top tips for budget-friendly travel and finding hidden gems.",
    metadata={
        "Domain": "Travel and Tourism",
        "Topic": "Travel Tips",
        "Category": "Budget Travel",
        "Published Date": "2023-09-28",
        "Source": "Travel Inspiration",
        "Author": "Alex Diaz",
        "Tags": ["Budget Travel", "Secrets"],
        "Keywords": ["travel tips", "hidden gems"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=5
)

document_6 = Document(
    page_content="Cultural festivals around the world attract tourists seeking immersive local experiences.",
    metadata={
        "Domain": "Travel and Tourism",
        "Topic": "Cultural Events",
        "Category": "Experiences",
        "Published Date": "2023-09-25",
        "Source": "Culture Travel Guide",
        "Author": "Brian Chen",
        "Tags": ["Festivals", "Culture"],
        "Keywords": ["cultural festivals", "local experiences"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=6
)

document_7 = Document(
    page_content="Increased interest in adventure travel is leading to new tour offerings and excursions.",
    metadata={
        "Domain": "Travel and Tourism",
        "Topic": "Adventure Travel",
        "Category": "Tourism Trends",
        "Published Date": "2023-10-02",
        "Source": "Adventure Travel Times",
        "Author": "Mia Kwan",
        "Tags": ["Adventure", "Tours"],
        "Keywords": ["adventure travel", "excursions"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=7
)

document_8 = Document(
    page_content="Digital nomads are choosing destinations with excellent internet and lifestyle amenities.",
    metadata={
        "Domain": "Travel and Tourism",
        "Topic": "Remote Work",
        "Category": "Digital Nomads",
        "Published Date": "2023-09-27",
        "Source": "Nomad Life Journal",
        "Author": "Alex Diaz",
        "Tags": ["Remote Work", "Destinations"],
        "Keywords": ["digital nomads", "remote work travel"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=8
)

document_9 = Document(
    page_content="Luxury travel markets are adapting luxurious accommodations with a focus on personalized experiences.",
    metadata={
        "Domain": "Travel and Tourism",
        "Topic": "Luxury Travel",
        "Category": "Personalization",
        "Published Date": "2023-10-04",
        "Source": "Luxury Travel Review",
        "Author": "Sarah Cole",
        "Tags": ["Luxury", "Personalized Experiences"],
        "Keywords": ["luxury travel", "personalization"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=9
)

document_10 = Document(
    page_content="Tourists are being encouraged to participate in local conservation efforts as part of eco-travel.",
    metadata={
        "Domain": "Travel and Tourism",
        "Topic": "Conservation",
        "Category": "Sustainability",
        "Published Date": "2023-09-22",
        "Source": "Eco Travel Journal",
        "Author": "Brian Chen",
        "Tags": ["Conservation", "Tourism"],
        "Keywords": ["eco-travel", "conservation"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=10
)

travel_tourism_docs = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
]

#Create Automotive Transportation Documents
document_1 = Document(
    page_content="Electric vehicles (EVs) continue to gain popularity as new models improve in range and affordability.",
    metadata={
        "Domain": "Automotive and Transportation",
        "Topic": "Electric Vehicles",
        "Category": "Market Trends",
        "Published Date": "2023-09-29",
        "Source": "Automotive News",
        "Author": "James Oliver",
        "Tags": ["EVs", "Affordability"],
        "Keywords": ["electric cars", "range improvement"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=1
)

document_2 = Document(
    page_content="Innovative public transit solutions are reducing congestion and improving urban air quality in major cities.",
    metadata={
        "Domain": "Automotive and Transportation",
        "Topic": "Public Transit",
        "Category": "Urban Planning",
        "Published Date": "2023-09-30",
        "Source": "City Transit Report",
        "Author": "Natalie Green",
        "Tags": ["Public Transit", "Urban Air Quality"],
        "Keywords": ["congestion reduction", "urban transit"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=2
)

document_3 = Document(
    page_content="New car safety features are being developed leveraging AI to prevent collisions and enhance driver assistance.",
    metadata={
        "Domain": "Automotive and Transportation",
        "Topic": "Safety",
        "Category": "Technology",
        "Published Date": "2023-10-01",
        "Source": "Tech in Autos Journal",
        "Author": "Tom Baker",
        "Tags": ["Safety", "AI"],
        "Keywords": ["collision prevention", "driver assistance"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=3
)

document_4 = Document(
    page_content="Autonomous vehicles are facing regulatory hurdles as authorities work on safety standards.",
    metadata={
        "Domain": "Automotive and Transportation",
        "Topic": "Autonomous Vehicles",
        "Category": "Regulations",
        "Published Date": "2023-09-23",
        "Source": "Auto Regulations Daily",
        "Author": "James Oliver",
        "Tags": ["Autonomous Vehicles", "Regulations"],
        "Keywords": ["autonomous cars", "safety standards"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=4
)

document_5 = Document(
    page_content="Bike-sharing programs are expanding globally, offering sustainable transportation in urban areas.",
    metadata={
        "Domain": "Automotive and Transportation",
        "Topic": "Bike Sharing",
        "Category": "Sustainability",
        "Published Date": "2023-09-25",
        "Source": "Cycle News Network",
        "Author": "Natalie Green",
        "Tags": ["Bike Sharing", "Urban Transport"],
        "Keywords": ["sustainable transport", "bike programs"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=5
)

document_6 = Document(
    page_content="The future of hybrid cars includes enhanced fuel efficiency and reduced emissions.",
    metadata={
        "Domain": "Automotive and Transportation",
        "Topic": "Hybrid Vehicles",
        "Category": "Innovation",
        "Published Date": "2023-09-28",
        "Source": "Hybrid Vehicle Times",
        "Author": "Tom Baker",
        "Tags": ["Hybrid Cars", "Efficiency"],
        "Keywords": ["fuel efficiency", "emissions reduction"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=6
)

document_7 = Document(
    page_content="Advancements in hydrogen fuel technology promise a cleaner alternative for long-distance transportation.",
    metadata={
        "Domain": "Automotive and Transportation",
        "Topic": "Hydrogen Technology",
        "Category": "Clean Energy",
        "Published Date": "2023-10-02",
        "Source": "Fuel Cell News",
        "Author": "James Oliver",
        "Tags": ["Hydrogen", "Clean Energy"],
        "Keywords": ["hydrogen fuel", "long-distance transport"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=7
)

document_8 = Document(
    page_content="New car subscription services are offering flexible vehicle access without the burden of ownership.",
    metadata={
        "Domain": "Automotive and Transportation",
        "Topic": "Car Subscriptions",
        "Category": "Service Models",
        "Published Date": "2023-09-27",
        "Source": "Auto Business Journal",
        "Author": "Natalie Green",
        "Tags": ["Car Subscriptions", "Service Innovations"],
        "Keywords": ["flexible vehicle access", "ownership alternatives"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=8
)

document_9 = Document(
    page_content="The rise of shared autonomous shuttles is reshaping last-mile transportation in urban areas.",
    metadata={
        "Domain": "Automotive and Transportation",
        "Topic": "Shared Mobility",
        "Category": "Urban Transport",
        "Published Date": "2023-09-22",
        "Source": "Shared Transport Digest",
        "Author": "Tom Baker",
        "Tags": ["Autonomous Shuttles", "Mobility"],
        "Keywords": ["shared transport", "autonomous vehicles"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=9
)

document_10 = Document(
    page_content="Improvements in freight logistics technology are enhancing efficiency in global goods transportation.",
    metadata={
        "Domain": "Automotive and Transportation",
        "Topic": "Freight",
        "Category": "Logistics",
        "Published Date": "2023-10-03",
        "Source": "Freight News Today",
        "Author": "James Oliver",
        "Tags": ["Freight Logistics", "Global Transport"],
        "Keywords": ["logistics technology", "efficiency"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=10
)

automotive_transportation_docs = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
]


#Create Education Academia docs
document_1 = Document(
    page_content="Remote learning continues to reshape educational landscapes, prompting increased use of digital tools.",
    metadata={
        "Domain": "Education and Academia",
        "Topic": "Remote Learning",
        "Category": "Digital Education",
        "Published Date": "2023-09-22",
        "Source": "Education Insights",
        "Author": "Benjamin Turner",
        "Tags": ["Remote Learning", "Digital Tools"],
        "Keywords": ["remote education", "e-learning"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=1
)

document_2 = Document(
    page_content="STEM education initiatives are expanding, encouraging more students to pursue science and technology careers.",
    metadata={
        "Domain": "Education and Academia",
        "Topic": "STEM Education",
        "Category": "Career Development",
        "Published Date": "2023-10-01",
        "Source": "STEM Education Today",
        "Author": "Linda Gomez",
        "Tags": ["STEM", "Careers"],
        "Keywords": ["STEM initiatives", "technology education"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=2
)

document_3 = Document(
    page_content="Higher education institutions are facing challenges from declining enrollment amid shifting student priorities.",
    metadata={
        "Domain": "Education and Academia",
        "Topic": "Higher Education",
        "Category": "Enrollment",
        "Published Date": "2023-09-27",
        "Source": "University Review",
        "Author": "Andrew Thompson",
        "Tags": ["Higher Education", "Enrollment"],
        "Keywords": ["college enrollment", "student priorities"],
        "Language": "English",
        "Sentiment": "Concerned"
    },
    id=3
)

document_4 = Document(
    page_content="Inclusive teaching methods are being adopted to accommodate diverse student learning needs.",
    metadata={
        "Domain": "Education and Academia",
        "Topic": "Inclusive Education",
        "Category": "Teaching Methods",
        "Published Date": "2023-10-03",
        "Source": "Teaching Insights",
        "Author": "Linda Gomez",
        "Tags": ["Inclusive Education", "Diversity"],
        "Keywords": ["inclusive teaching", "diverse learning"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=4
)

document_5 = Document(
    page_content="Teachers are increasingly using technology to personalize student learning experiences and improve outcomes.",
    metadata={
        "Domain": "Education and Academia",
        "Topic": "EdTech",
        "Category": "Personalized Learning",
        "Published Date": "2023-09-28",
        "Source": "EdTech Updates",
        "Author": "Benjamin Turner",
        "Tags": ["Technology", "Personalized Learning"],
        "Keywords": ["edtech", "learning outcomes"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=5
)

document_6 = Document(
    page_content="Students' mental health is being prioritized as part of holistic education approaches in schools.",
    metadata={
        "Domain": "Education and Academia",
        "Topic": "Student Health",
        "Category": "Wellbeing",
        "Published Date": "2023-09-30",
        "Source": "Education Health Report",
        "Author": "Andrew Thompson",
        "Tags": ["Mental Health", "Education"],
        "Keywords": ["student wellbeing", "holistic approaches"],
        "Language": "English",
        "Sentiment": "Concerned"
    },
    id=6
)

document_7 = Document(
    page_content="Lifelong learning is emphasizing continuous skills upgrading in response to a rapidly changing job market.",
    metadata={
        "Domain": "Education and Academia",
        "Topic": "Adult Education",
        "Category": "Lifelong Learning",
        "Published Date": "2023-10-04",
        "Source": "Adult Learning News",
        "Author": "Linda Gomez",
        "Tags": ["Lifelong Learning", "Career Skills"],
        "Keywords": ["skills upgrading", "job market"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=7
)

document_8 = Document(
    page_content="The integration of gamification in education aims to increase student engagement and learning motivation.",
    metadata={
        "Domain": "Education and Academia",
        "Topic": "Gamification",
        "Category": "Student Engagement",
        "Published Date": "2023-09-26",
        "Source": "Education Games Review",
        "Author": "Benjamin Turner",
        "Tags": ["Gamification", "Motivation"],
        "Keywords": ["education games", "student motivation"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=8
)

document_9 = Document(
    page_content="New educational policies are being developed to address disparities in school funding.",
    metadata={
        "Domain": "Education and Academia",
        "Topic": "Education Policy",
        "Category": "Funding",
        "Published Date": "2023-09-22",
        "Source": "Policy Education Review",
        "Author": "Andrew Thompson",
        "Tags": ["Policy", "Funding"],
        "Keywords": ["education policy", "school funding"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=9
)

document_10 = Document(
    page_content="Digital literacy programs underscore their importance as part of curricula in educational institutions.",
    metadata={
        "Domain": "Education and Academia",
        "Topic": "Digital Literacy",
        "Category": "Curriculum",
        "Published Date": "2023-10-06",
        "Source": "Digital Education News",
        "Author": "Linda Gomez",
        "Tags": ["Digital Literacy", "Curriculum"],
        "Keywords": ["digital skills", "education programs"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=10
)

document_11 = Document(
    page_content="Online education platforms are enhancing accessibility to wide-ranging learning materials and expert instructors.",
    metadata={
        "Domain": "Education and Academia",
        "Topic": "Online Education",
        "Category": "Accessibility",
        "Published Date": "2023-09-29",
        "Source": "EdTech Access Journal",
        "Author": "Benjamin Turner",
        "Tags": ["Online Learning", "Access"],
        "Keywords": ["education platforms", "learning access"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=11
)

document_12 = Document(
    page_content="Bilingual education programs foster language skills and cultural appreciation among students.",
    metadata={
        "Domain": "Education and Academia",
        "Topic": "Bilingual Education",
        "Category": "Language Learning",
        "Published Date": "2023-10-07",
        "Source": "Language Education Review",
        "Author": "Andrew Thompson",
        "Tags": ["Bilingual", "Cultural Appreciation"],
        "Keywords": ["language skills", "education"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=12
)

education_academia_docs = [    
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
    document_11,
    document_12
]

#Create Environment Sustainability Documents
document_1 = Document(
    page_content="The latest climate report reveals a rapid increase in global temperatures, stressing urgent action.",
    metadata={
        "Domain": "Environment and Sustainability",
        "Topic": "Climate Change",
        "Category": "Global Warming",
        "Published Date": "2023-10-03",
        "Source": "Climate News Network",
        "Author": "Laura Chang",
        "Tags": "Climate Change, Global Warming",
        "Keywords": "temperature rise, climate report",
        "Language": "English",
        "Sentiment": "Concerned"
    },
    id=1
)

document_2 = Document(
    page_content="Sustainable agriculture practices are key to reducing environmental impact while boosting crop yield.",
    metadata={
        "Domain": "Environment and Sustainability",
        "Topic": "Sustainable Agriculture",
        "Category": "Practices",
        "Published Date": "2023-10-01",
        "Source": "Eco Farming Journal",
        "Author": "David Smith",
        "Tags": "Agriculture, Sustainability",
        "Keywords": "sustainable farming, environmental impact",
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=2
)

document_3 = Document(
    page_content="Innovative renewable energy projects are being implemented to replace fossil fuels and reduce emissions.",
    metadata={
        "Domain": "Environment and Sustainability",
        "Topic": "Renewable Energy",
        "Category": "Innovation",
        "Published Date": "2023-09-30",
        "Source": "Green Tech Digest",
        "Author": "Emily Reynolds",
        "Tags": "Renewables, Innovation",
        "Keywords": "renewable energy, fossil fuels",
        "Language": "English",
        "Sentiment": "Optimistic"
    },
    id=3
)

document_4 = Document(
    page_content="Our oceans are facing unprecedented levels of pollution, harming marine biodiversity significantly.",
    metadata={
        "Domain": "Environment and Sustainability",
        "Topic": "Marine Pollution",
        "Category": "Biodiversity Loss",
        "Published Date": "2023-09-27",
        "Source": "Marine Environment News",
        "Author": "Laura Chang",
        "Tags": "Pollution, Marine Biodiversity",
        "Keywords": "ocean pollution, biodiversity",
        "Language": "English",
        "Sentiment": "Alarmed"
    },
    id=4
)

document_5 = Document(
    page_content="Community-driven recycling initiatives show substantial reduction in local waste production.",
    metadata={
        "Domain": "Environment and Sustainability",
        "Topic": "Recycling",
        "Category": "Community Initiatives",
        "Published Date": "2023-10-04",
        "Source": "Eco Community Journal",
        "Author": "David Smith",
        "Tags": "Recycling, Waste Management",
        "Keywords": "community recycling, waste reduction",
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=5
)

document_6 = Document(
    page_content="Deforestation rates are declining in regions that adopt reforestation and conservation strategies.",
    metadata={
        "Domain": "Environment and Sustainability",
        "Topic": "Deforestation",
        "Category": "Conservation",
        "Published Date": "2023-09-25",
        "Source": "Conservation News",
        "Author": "Emily Reynolds",
        "Tags": "Deforestation, Conservation",
        "Keywords": "deforestation, reforestation",
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=6
)

document_7 = Document(
    page_content="Electric vehicle adoption is accelerating, promising a significant decrease in transportation emissions.",
    metadata={
        "Domain": "Environment and Sustainability",
        "Topic": "Electric Vehicles",
        "Category": "Transportation",
        "Published Date": "2023-09-28",
        "Source": "Eco Transport Review",
        "Author": "Laura Chang",
        "Tags": "EVs, Emissions Reduction",
        "Keywords": "electric vehicles, transport emissions",
        "Language": "English",
        "Sentiment": "Optimistic"
    },
    id=7
)

document_8 = Document(
    page_content="Innovative water conservation techniques are being developed to address global water scarcity issues.",
    metadata={
        "Domain": "Environment and Sustainability",
        "Topic": "Water Conservation",
        "Category": "Resource Management",
        "Published Date": "2023-09-21",
        "Source": "Water Management News",
        "Author": "David Smith",
        "Tags": "Water Conservation, Scarcity",
        "Keywords": "water conservation, scarcity solutions",
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=8
)

document_9 = Document(
    page_content="Eco-tourism practices are encouraging sustainable travel and contributing to local economies.",
    metadata={
        "Domain": "Environment and Sustainability",
        "Topic": "Eco-tourism",
        "Category": "Travel",
        "Published Date": "2023-10-05",
        "Source": "Green Travel Review",
        "Author": "Emily Reynolds",
        "Tags": "Eco-tourism, Sustainability",
        "Keywords": "sustainable travel, local economy",
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=9
)

document_10 = Document(
    page_content="Cities investing in green infrastructure are seeing improvements in urban resilience and quality of life.",
    metadata={
        "Domain": "Environment and Sustainability",
        "Topic": "Urban Development",
        "Category": "Green Infrastructure",
        "Published Date": "2023-09-24",
        "Source": "Urban Green News",
        "Author": "Laura Chang",
        "Tags": "Urban Development, Quality of Life",
        "Keywords": "green infrastructure, urban resilience",
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=10
)

document_11 = Document(
    page_content="Strategies for reducing plastic consumption are gaining traction among consumers and industries.",
    metadata={
        "Domain": "Environment and Sustainability",
        "Topic": "Plastic Reduction",
        "Category": "Waste Management",
        "Published Date": "2023-10-06",
        "Source": "Sustainable Living Digest",
        "Author": "David Smith",
        "Tags": "Plastic, Waste Management",
        "Keywords": "plastic reduction, consumer strategies",
        "Language": "English",
        "Sentiment": "Optimistic"
    },
    id=11
)

environment_sustainability_docs = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
    document_11
]

#Create Finance Economics Documents
document_1 = Document(
    page_content="Interest rate hikes loom as inflation fears persist in the current economic climate.",
    metadata={
        "Domain": "Finance and Economics",
        "Topic": "Monetary Policy",
        "Category": "Interest Rates",
        "Published Date": "2023-09-29",
        "Source": "Economic Times",
        "Author": "Jane Smith",
        "Tags": ["Interest Rates", "Inflation"],
        "Keywords": ["economy", "inflation", "interest hike"],
        "Language": "English",
        "Sentiment": "Concerned"
    },
    id=1
)

document_2 = Document(
    page_content="Record-breaking quarterly profits are reported by leading tech companies amid high demand for digital services.",
    metadata={
        "Domain": "Finance and Economics",
        "Topic": "Corporate Earnings",
        "Category": "Technology",
        "Published Date": "2023-09-30",
        "Source": "Market Watcher",
        "Author": "Michael Green",
        "Tags": ["Earnings", "Tech"],
        "Keywords": ["profits", "digital services", "tech industry"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=2
)

document_3 = Document(
    page_content="The global cryptocurrency market experiences volatility amid regulatory changes in major economies.",
    metadata={
        "Domain": "Finance and Economics",
        "Topic": "Cryptocurrency",
        "Category": "Market Dynamics",
        "Published Date": "2023-10-03",
        "Source": "Crypto News",
        "Author": "Lily Brown",
        "Tags": ["Cryptocurrency", "Regulation"],
        "Keywords": ["market volatility", "crypto regulation"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=3
)

document_4 = Document(
    page_content="Housing market shows signs of cooling after a prolonged period of rapid price increases.",
    metadata={
        "Domain": "Finance and Economics",
        "Topic": "Real Estate",
        "Category": "Market Trends",
        "Published Date": "2023-09-25",
        "Source": "Real Estate Digest",
        "Author": "Jane Smith",
        "Tags": ["Housing", "Market Trends"],
        "Keywords": ["housing market", "cooling trends"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=4
)

document_5 = Document(
    page_content="Job creation rates surpass expectations, marking a robust economic recovery from the last recession.",
    metadata={
        "Domain": "Finance and Economics",
        "Topic": "Labor Market",
        "Category": "Job Growth",
        "Published Date": "2023-10-06",
        "Source": "Economic Outlook",
        "Author": "Michael Green",
        "Tags": ["Job Growth", "Recovery"],
        "Keywords": ["employment", "economic recovery"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=5
)

document_6 = Document(
    page_content="Increasing interest in sustainable investing drives shifts in financial markets worldwide.",
    metadata={
        "Domain": "Finance and Economics",
        "Topic": "Sustainable Finance",
        "Category": "Investment Trends",
        "Published Date": "2023-09-20",
        "Source": "Investment Journal",
        "Author": "Lily Brown",
        "Tags": ["Sustainable Investing", "Markets"],
        "Keywords": ["investment trends", "sustainability"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=6
)

document_7 = Document(
    page_content="Innovative fintech solutions are revolutionizing the financial sector, offering greater accessibility.",
    metadata={
        "Domain": "Finance and Economics",
        "Topic": "Fintech",
        "Category": "Innovation",
        "Published Date": "2023-09-27",
        "Source": "Fintech Review",
        "Author": "Jane Smith",
        "Tags": ["Innovation", "Fintech"],
        "Keywords": ["fintech solutions", "financial innovation"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=7
)

document_8 = Document(
    page_content="Major stock indices see renewed optimism after successful trade negotiations with international partners.",
    metadata={
        "Domain": "Finance and Economics",
        "Topic": "Stock Market",
        "Category": "Trade",
        "Published Date": "2023-10-03",
        "Source": "Financial Bulletin",
        "Author": "Michael Green",
        "Tags": ["Stock Market", "Trade Negotiations"],
        "Keywords": ["stock market", "trade success"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=8
)

document_9 = Document(
    page_content="The impact of AI on the job market creates debates over future employment dynamics.",
    metadata={
        "Domain": "Finance and Economics",
        "Topic": "Artificial Intelligence",
        "Category": "Employment",
        "Published Date": "2023-09-25",
        "Source": "Tech Economics",
        "Author": "Lily Brown",
        "Tags": ["AI", "Employment"],
        "Keywords": ["AI impact", "job market"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=9
)

document_10 = Document(
    page_content="Global supply chain disruptions continue to challenge businesses across various industries.",
    metadata={
        "Domain": "Finance and Economics",
        "Topic": "Supply Chain",
        "Category": "Disruptions",
        "Published Date": "2023-10-01",
        "Source": "Business Insights",
        "Author": "Jane Smith",
        "Tags": ["Supply Chain", "Challenges"],
        "Keywords": ["global disruptions", "business challenges"],
        "Language": "English",
        "Sentiment": "Concerned"
    },
    id=10
)

document_11 = Document(
    page_content="Consumer spending patterns adapt as economic conditions and consumer behaviors evolve.",
    metadata={
        "Domain": "Finance and Economics",
        "Topic": "Consumer Behavior",
        "Category": "Economy",
        "Published Date": "2023-10-04",
        "Source": "Market Analysis",
        "Author": "Michael Green",
        "Tags": ["Consumer Behavior", "Economy"],
        "Keywords": ["spending patterns", "economic change"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=11
)

finance_economics_docs = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
    document_11
]

#Create Healthcare Medicine Documents
document_1 = Document(
    page_content="A recent study found daily jogging significantly reduces the risk of cardiovascular disease in adults.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Cardiovascular Diseases",
        "Category": "Preventive Healthcare",
        "Published Date": "2023-10-02",
        "Source": "Journal of Medicine",
        "Author": "Dr. Emily Sanders",
        "Tags": ["Health", "Exercise"],
        "Keywords": ["heart disease", "jogging", "prevention"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=1
)

document_2 = Document(
    page_content="Innovative AI technology is now assisting doctors in diagnosing complex medical conditions quicker than before.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Medical Technology",
        "Category": "Innovation",
        "Published Date": "2023-09-28",
        "Source": "HealthTech News",
        "Author": "Alex Johnson",
        "Tags": ["AI", "Diagnosis"],
        "Keywords": ["innovation", "technology", "medical diagnosis"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=2
)

document_3 = Document(
    page_content="Researchers have identified a compound in blueberries that may improve memory in older adults.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Nutrition",
        "Category": "Research",
        "Published Date": "2023-10-05",
        "Source": "Nutrition Weekly",
        "Author": "Samantha Lee",
        "Tags": ["Research", "Memory"],
        "Keywords": ["blueberries", "memory", "older adults"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=3
)

document_4 = Document(
    page_content="Telehealth services continue to rise in popularity, providing greater access to rural and underserved areas.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Telehealth",
        "Category": "Access",
        "Published Date": "2023-09-15",
        "Source": "Health News Daily",
        "Author": "Dr. Chris Miller",
        "Tags": ["Telehealth", "Accessibility"],
        "Keywords": ["digital health", "access", "rural"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=4
)

document_5 = Document(
    page_content="Vitamin D deficiency remains a widespread issue, especially in regions with limited sunlight during winter.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Vitamins",
        "Category": "Deficiency",
        "Published Date": "2023-10-07",
        "Source": "Medical Journal Review",
        "Author": "Dr. Emily Sanders",
        "Tags": ["Vitamin D", "Health Risks"],
        "Keywords": ["deficiency", "health", "winter"],
        "Language": "English",
        "Sentiment": "Concerned"
    },
    id=5
)

document_6 = Document(
    page_content="Exercise not only improves physical wellbeing but also has profound benefits for mental health.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Mental Health",
        "Category": "Benefits of Exercise",
        "Published Date": "2023-09-30",
        "Source": "Wellness Daily",
        "Author": "Alex Johnson",
        "Tags": ["Exercise", "Mental Health"],
        "Keywords": ["exercise benefits", "mental health", "wellbeing"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=6
)

document_7 = Document(
    page_content="Childhood obesity rates continue to climb, prompting a call for wider public health interventions.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Obesity",
        "Category": "Public Health",
        "Published Date": "2023-10-08",
        "Source": "Health Policy News",
        "Author": "Samantha Lee",
        "Tags": ["Public Health", "Obesity"],
        "Keywords": ["childhood obesity", "health interventions"],
        "Language": "English",
        "Sentiment": "Concerned"
    },
    id=7
)

document_8 = Document(
    page_content="A new breakthrough drug for combating Alzheimer’s disease could improve the quality of life for many patients.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Alzheimer’s Disease",
        "Category": "Treatment",
        "Published Date": "2023-09-25",
        "Source": "Pharma News",
        "Author": "Dr. Chris Miller",
        "Tags": ["Alzheimer’s", "Treatment"],
        "Keywords": ["breakthrough", "drug", "patient care"],
        "Language": "English",
        "Sentiment": "Optimistic"
    },
    id=8
)

document_9 = Document(
    page_content="Healthcare costs rise again, prompting calls for reform and policy changes to ease the burden on families.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Healthcare Costs",
        "Category": "Policy",
        "Published Date": "2023-10-01",
        "Source": "Policy Review",
        "Author": "Alex Johnson",
        "Tags": ["Healthcare", "Policy"],
        "Keywords": ["reform", "healthcare costs", "policy change"],
        "Language": "English",
        "Sentiment": "Concerned"
    },
    id=9
)

document_10 = Document(
    page_content="Adopting a plant-based diet may significantly reduce one's risk of developing chronic illnesses.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Diet",
        "Category": "Preventive Strategies",
        "Published Date": "2023-09-18",
        "Source": "Health Magazine",
        "Author": "Samantha Lee",
        "Tags": ["Diet", "Chronic Illness"],
        "Keywords": ["plant-based diet", "health prevention", "chronic disease"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=10
)

document_11 = Document(
    page_content="Latest findings indicate that probiotics support gut health and could strengthen the immune system.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Gut Health",
        "Category": "Research",
        "Published Date": "2023-09-20",
        "Source": "Gut Health Today",
        "Author": "Dr. Emily Sanders",
        "Tags": ["Probiotics", "Immune System"],
        "Keywords": ["gut health", "probiotics", "immune support"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=11
)

document_12 = Document(
    page_content="The influence of climate change on the spread of vector-borne diseases is an emerging concern.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Infectious Diseases",
        "Category": "Environmental Impact",
        "Published Date": "2023-10-04",
        "Source": "Environmental Health Digest",
        "Author": "Alex Johnson",
        "Tags": ["Climate Change", "Disease Spread"],
        "Keywords": ["vector-borne diseases", "climate impact"],
        "Language": "English",
        "Sentiment": "Concerned"
    },
    id=12
)

document_13 = Document(
    page_content="Mindfulness meditation is found to lower stress levels and enhance overall mental clarity.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Mental Health",
        "Category": "Mindfulness",
        "Published Date": "2023-10-02",
        "Source": "Calm Mind Journal",
        "Author": "Samantha Lee",
        "Tags": ["Mindfulness", "Mental Clarity"],
        "Keywords": ["meditation", "stress reduction", "mental health"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=13
)

document_14 = Document(
    page_content="Heart health guidelines emphasized the importance of routine screenings and lifestyle modifications.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Heart Health",
        "Category": "Guidelines",
        "Published Date": "2023-09-30",
        "Source": "Heart Health Monitor",
        "Author": "Dr. Chris Miller",
        "Tags": ["Screening", "Lifestyle"],
        "Keywords": ["heart screening", "lifestyle change", "heart health"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=14
)

document_15 = Document(
    page_content="Public initiatives to lower childhood obesity rates are gaining momentum with promising results.",
    metadata={
        "Domain": "Healthcare and Medicine",
        "Topic": "Public Health",
        "Category": "Childhood Obesity",
        "Published Date": "2023-09-24",
        "Source": "Public Health Review",
        "Author": "Dr. Emily Sanders",
        "Tags": ["Public Initiatives", "Obesity"],
        "Keywords": ["childhood obesity", "public health"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=15
)

healthcare_medicine_docs = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
    document_11,
    document_12,
    document_13,
    document_14,
    document_15
]

#Create Retail Commerce Documents
document_1 = Document(
    page_content="E-commerce giants are expanding their logistics networks to meet increasing consumer demand for faster delivery.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Logistics",
        "Category": "Supply Chain",
        "Published Date": "2023-09-18",
        "Source": "Retail News Daily",
        "Author": "Sophia Kim",
        "Tags": ["E-commerce", "Logistics"],
        "Keywords": ["consumer demand", "fast delivery"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=1
)

document_2 = Document(
    page_content="The rise of mobile shopping apps is transforming how consumers engage with online shopping platforms.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Mobile Shopping",
        "Category": "Consumer Behavior",
        "Published Date": "2023-10-02",
        "Source": "Tech Retail Watch",
        "Author": "John Lester",
        "Tags": ["Mobile Apps", "Consumer Engagement"],
        "Keywords": ["mobile shopping", "engagement"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=2
)

document_3 = Document(
    page_content="Retailers are adopting augmented reality to offer customers virtual try-ons and enhance the shopping experience.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Augmented Reality",
        "Category": "Customer Experience",
        "Published Date": "2023-09-26",
        "Source": "Innovative Retailer",
        "Author": "Emma Patel",
        "Tags": ["AR", "Virtual Try-on"],
        "Keywords": ["enhanced shopping", "augmented reality"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=3
)

document_4 = Document(
    page_content="Sustainable shopping practices are becoming popular as consumers show increased interest in eco-friendly products.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Sustainability",
        "Category": "Consumer Trends",
        "Published Date": "2023-09-30",
        "Source": "Eco Retail Insights",
        "Author": "Sophia Kim",
        "Tags": ["Sustainability", "Eco-friendly"],
        "Keywords": ["sustainable shopping", "eco trends"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=4
)

document_5 = Document(
    page_content="The integration of AI in e-commerce is personalizing recommendations, enhancing customer satisfaction and sales.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Artificial Intelligence",
        "Category": "Personalization",
        "Published Date": "2023-10-03",
        "Source": "AI Retail Journal",
        "Author": "Liam Green",
        "Tags": ["AI", "Recommendations"],
        "Keywords": ["personalized shopping", "customer satisfaction"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=5
)

document_6 = Document(
    page_content="Flash sales and limited-time offers continue to drive e-commerce purchases, creating a sense of urgency.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Sales Strategies",
        "Category": "Marketing",
        "Published Date": "2023-09-28",
        "Source": "Marketing Today",
        "Author": "Emma Patel",
        "Tags": ["Sales", "Urgency"],
        "Keywords": ["flash sales", "marketing strategies"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=6
)

document_7 = Document(
    page_content="Social commerce is gaining momentum, with platforms integrating shopping features directly into social media.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Social Commerce",
        "Category": "Trends",
        "Published Date": "2023-09-24",
        "Source": "Social Retail Watch",
        "Author": "John Lester",
        "Tags": ["Social Media", "Commerce"],
        "Keywords": ["social shopping", "platforms"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=7
)

document_8 = Document(
    page_content="B2B e-commerce is evolving, focusing on improving efficiency and streamlining business transactions.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "B2B",
        "Category": "Business Solutions",
        "Published Date": "2023-09-21",
        "Source": "B2B Innovations",
        "Author": "Liam Green",
        "Tags": ["B2B", "E-commerce"],
        "Keywords": ["business efficiency", "transaction solutions"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=8
)

document_9 = Document(
    page_content="E-commerce platforms are enhancing cybersecurity measures to protect consumers from online threats.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Cybersecurity",
        "Category": "Protection",
        "Published Date": "2023-10-04",
        "Source": "Cyber Retail News",
        "Author": "Emma Patel",
        "Tags": ["E-commerce", "Security"],
        "Keywords": ["consumer protection", "online threats"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=9
)

document_10 = Document(
    page_content="Data analytics are driving retail strategies, enabling personalized consumer experiences and more effective marketing.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Data Analytics",
        "Category": "Strategy",
        "Published Date": "2023-10-05",
        "Source": "Retail Analytics Digest",
        "Author": "Sophia Kim",
        "Tags": ["Data", "Strategy"],
        "Keywords": ["analytics", "personalized marketing"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=10
)

document_11 = Document(
    page_content="Retailers embracing omnichannel strategies are finding success in integrating physical and digital shopping experiences.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Omnichannel",
        "Category": "Integration",
        "Published Date": "2023-09-26",
        "Source": "OmniRetail Insights",
        "Author": "John Lester",
        "Tags": ["Omnichannel", "Integration"],
        "Keywords": ["retail strategy", "digital integration"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=11
)

document_12 = Document(
    page_content="VR in retail is creating immersive shopping experiences, revolutionizing how customers interact with brands.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Virtual Reality",
        "Category": "Innovation",
        "Published Date": "2023-09-30",
        "Source": "VR Retail Magazine",
        "Author": "Liam Green",
        "Tags": ["VR", "Retail"],
        "Keywords": ["immersive shopping", "brand interaction"],
        "Language": "English",
        "Sentiment": "Excited"
    },
    id=12
)

document_13 = Document(
    page_content="The increasing importance of ethical sourcing in e-commerce is shaping consumer purchasing decisions.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Ethical Sourcing",
        "Category": "Consumer Trends",
        "Published Date": "2023-10-06",
        "Source": "Ethical Commerce Journal",
        "Author": "Emma Patel",
        "Tags": ["Ethics", "Sourcing"],
        "Keywords": ["ethical sourcing", "consumer behavior"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=13
)

document_14 = Document(
    page_content="The rise of subscription box services is providing consumers with new ways to discover and enjoy products regularly.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Subscription Services",
        "Category": "Innovation",
        "Published Date": "2023-10-02",
        "Source": "Retail Subscription News",
        "Author": "Sophia Kim",
        "Tags": ["Subscription", "Discovery"],
        "Keywords": ["subscriptions", "consumer experience"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=14
)

document_15 = Document(
    page_content="Cross-border e-commerce is expanding, breaking down international trade barriers and enhancing consumer access to global markets.",
    metadata={
        "Domain": "Retail and E-commerce",
        "Topic": "Cross-Border",
        "Category": "Global Market",
        "Published Date": "2023-09-24",
        "Source": "Global Retail Insights",
        "Author": "John Lester",
        "Tags": ["International", "Trade"],
        "Keywords": ["global e-commerce", "trade barriers"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=15
)

retail_ecommerce_docs = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
    document_11,
    document_12,
    document_13,
    document_14,
    document_15
]

#Create Sports Fitness Documents
document_1 = Document(
    page_content="The importance of stretching before workouts to prevent injuries and improve flexibility cannot be overstated.",
    metadata={
        "Domain": "Sports and Fitness",
        "Topic": "Sports Health",
        "Category": "Injury Prevention",
        "Published Date": "2023-09-21",
        "Source": "Fitness Health Journal",
        "Author": "Jordan Lee",
        "Tags": ["Stretching", "Injury Prevention"],
        "Keywords": ["workout", "flexibility"],
        "Language": "English",
        "Sentiment": "Informative"
    },
    id=1
)

document_2 = Document(
    page_content="Professional athletes discuss their personal training regimes and nutritional plans for optimal performance.",
    metadata={
        "Domain": "Sports and Fitness",
        "Topic": "Athlete Training",
        "Category": "Personal Regimes",
        "Published Date": "2023-09-30",
        "Source": "Athlete Insights Magazine",
        "Author": "Melissa Carter",
        "Tags": ["Athletes", "Training"],
        "Keywords": ["training regimes", "nutrition"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=2
)

document_3 = Document(
    page_content="Walking and cycling are increasingly popular as both fitness practices and sustainable transportation.",
    metadata={
        "Domain": "Sports and Fitness",
        "Topic": "Fitness",
        "Category": "Sustainability",
        "Published Date": "2023-10-01",
        "Source": "Active Living News",
        "Author": "Casey Grant",
        "Tags": ["Cycling", "Walking"],
        "Keywords": ["fitness", "sustainability"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=3
)

document_4 = Document(
    page_content="Recent research underscores the benefits of high-intensity interval training (HIIT) for cardiovascular health.",
    metadata={
        "Domain": "Sports and Fitness",
        "Topic": "Cardiovascular Fitness",
        "Category": "Research",
        "Published Date": "2023-09-23",
        "Source": "Health Science Reports",
        "Author": "Jordan Lee",
        "Tags": ["HIIT", "Cardiovascular Health"],
        "Keywords": ["HIIT", "heart health"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=4
)

document_5 = Document(
    page_content="Yoga and meditation practices are being integrated into athletic training for mental resilience.",
    metadata={
        "Domain": "Sports and Fitness",
        "Topic": "Mental Health",
        "Category": "Training Strategies",
        "Published Date": "2023-09-28",
        "Source": "Zen Athlete Journal",
        "Author": "Melissa Carter",
        "Tags": ["Yoga", "Meditation"],
        "Keywords": ["mental resilience", "athletic training"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=5
)

document_6 = Document(
    page_content="New nutrition guidelines for athletes focus on recovery and muscle-building through balanced diets.",
    metadata={
        "Domain": "Sports and Fitness",
        "Topic": "Sports Nutrition",
        "Category": "Guidelines",
        "Published Date": "2023-09-25",
        "Source": "Nutrition for Athletes",
        "Author": "Casey Grant",
        "Tags": ["Nutrition", "Recovery"],
        "Keywords": ["nutrition guidelines", "muscle building"],
        "Language": "English",
        "Sentiment": "Informative"
    },
    id=6
)

document_7 = Document(
    page_content="Virtual races and competitions gain popularity, providing new opportunities for community engagement.",
    metadata={
        "Domain": "Sports and Fitness",
        "Topic": "Community Sports",
        "Category": "Virtual Events",
        "Published Date": "2023-10-02",
        "Source": "Sports Community Review",
        "Author": "Jordan Lee",
        "Tags": ["Virtual Races", "Community"],
        "Keywords": ["virtual events", "sports community"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=7
)

document_8 = Document(
    page_content="Strength training benefits for older adults are highlighted through recent health studies.",
    metadata={
        "Domain": "Sports and Fitness",
        "Topic": "Aging and Fitness",
        "Category": "Research",
        "Published Date": "2023-09-29",
        "Source": "Health Aging Journal",
        "Author": "Melissa Carter",
        "Tags": ["Strength Training", "Older Adults"],
        "Keywords": ["fitness for aging", "strength benefits"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=8
)

document_9 = Document(
    page_content="The psychological benefits of team sports contribute significantly to youth development and social skills.",
    metadata={
        "Domain": "Sports and Fitness",
        "Topic": "Youth Sports",
        "Category": "Psychological Benefits",
        "Published Date": "2023-09-26",
        "Source": "Youth Sports Insight",
        "Author": "Casey Grant",
        "Tags": ["Team Sports", "Youth Development"],
        "Keywords": ["psychological benefits", "youth sports"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=9
)

document_10 = Document(
    page_content="Recent breakthroughs in wearable fitness technology are improving data accuracy in personal training.",
    metadata={
        "Domain": "Sports and Fitness",
        "Topic": "Technology",
        "Category": "Advancements",
        "Published Date": "2023-10-05",
        "Source": "Fitness Tech Trends",
        "Author": "Jordan Lee",
        "Tags": ["Wearable Tech", "Fitness"],
        "Keywords": ["wearable tech", "training accuracy"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=10
)

sports_fitness_docs = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
]

#Create Technology Innovation Docs
document_1 = Document(
    page_content="Quantum computing emerges as a transformative technology in solving complex mathematical problems.",
    metadata={
        "Domain": "Technology and Innovation",
        "Topic": "Quantum Computing",
        "Category": "Technology",
        "Published Date": "2023-09-21",
        "Source": "Tech Daily",
        "Author": "Sophia Nguyen",
        "Tags": ["Quantum", "Computing"],
        "Keywords": ["quantum computing", "complex problems"],
        "Language": "English",
        "Sentiment": "Optimistic"
    },
    id=1
)

document_2 = Document(
    page_content="Advancements in AI are reshaping healthcare with more accurate diagnostic tools and treatment.",
    metadata={
        "Domain": "Technology and Innovation",
        "Topic": "Artificial Intelligence",
        "Category": "Healthcare Innovation",
        "Published Date": "2023-09-28",
        "Source": "AI Health News",
        "Author": "Carl White",
        "Tags": ["AI", "Healthcare"],
        "Keywords": ["AI advancements", "diagnostic tools"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=2
)

document_3 = Document(
    page_content="The rise of blockchain technology is revolutionizing data security and financial transactions.",
    metadata={
        "Domain": "Technology and Innovation",
        "Topic": "Blockchain",
        "Category": "Data Security",
        "Published Date": "2023-10-02",
        "Source": "Blockchain Today",
        "Author": "Amelia Reed",
        "Tags": ["Blockchain", "Security"],
        "Keywords": ["blockchain", "financial security"],
        "Language": "English",
        "Sentiment": "Optimistic"
    },
    id=3
)

document_4 = Document(
    page_content="5G technology rollout improves connectivity, enabling faster and more reliable mobile services.",
    metadata={
        "Domain": "Technology and Innovation",
        "Topic": "5G Technology",
        "Category": "Connectivity",
        "Published Date": "2023-09-30",
        "Source": "Tech Insights",
        "Author": "Sophia Nguyen",
        "Tags": ["5G", "Connectivity"],
        "Keywords": ["5G rollout", "mobile services"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=4
)

document_5 = Document(
    page_content="Virtual reality is gaining traction in education, providing immersive learning experiences.",
    metadata={
        "Domain": "Technology and Innovation",
        "Topic": "Virtual Reality",
        "Category": "Education",
        "Published Date": "2023-09-26",
        "Source": "VR Education Journal",
        "Author": "Carl White",
        "Tags": ["VR", "Education"],
        "Keywords": ["virtual reality", "immersive learning"],
        "Language": "English",
        "Sentiment": "Optimistic"
    },
    id=5
)

document_6 = Document(
    page_content="Renewable energy technologies are developing to meet increasing global energy demands sustainably.",
    metadata={
        "Domain": "Technology and Innovation",
        "Topic": "Renewable Energy",
        "Category": "Sustainability",
        "Published Date": "2023-09-29",
        "Source": "Energy Innovations",
        "Author": "Amelia Reed",
        "Tags": ["Renewable Energy", "Sustainability"],
        "Keywords": ["renewables", "energy demands"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=6
)

document_7 = Document(
    page_content="Robotics advancements are diversifying into various industries, automating complex processes.",
    metadata={
        "Domain": "Technology and Innovation",
        "Topic": "Robotics",
        "Category": "Automation",
        "Published Date": "2023-10-05",
        "Source": "Robotics World",
        "Author": "Sophia Nguyen",
        "Tags": ["Robotics", "Automation"],
        "Keywords": ["robotics", "industrial automation"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=7
)

document_8 = Document(
    page_content="Wearable technology is becoming a cornerstone in personal health tracking and management.",
    metadata={
        "Domain": "Technology and Innovation",
        "Topic": "Wearables",
        "Category": "Health Tech",
        "Published Date": "2023-09-24",
        "Source": "Tech Health Reports",
        "Author": "Carl White",
        "Tags": ["Wearables", "Health Tracking"],
        "Keywords": ["wearables", "personal health"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=8
)

document_9 = Document(
    page_content="Internet of Things (IoT) expansion connects more devices, optimizing resource management.",
    metadata={
        "Domain": "Technology and Innovation",
        "Topic": "IoT",
        "Category": "Innovation",
        "Published Date": "2023-10-06",
        "Source": "IoT Innovation Journal",
        "Author": "Amelia Reed",
        "Tags": ["IoT", "Resource Management"],
        "Keywords": ["IoT", "connected devices"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=9
)

document_10 = Document(
    page_content="Cybersecurity evolves rapidly to protect against increasingly sophisticated digital threats.",
    metadata={
        "Domain": "Technology and Innovation",
        "Topic": "Cybersecurity",
        "Category": "Technology",
        "Published Date": "2023-10-07",
        "Source": "Cybersecurity Updates",
        "Author": "Sophia Nguyen",
        "Tags": ["Cybersecurity", "Digital Security"],
        "Keywords": ["cybersecurity", "digital threats"],
        "Language": "English",
        "Sentiment": "Neutral"
    },
    id=10
)

document_11 = Document(
    page_content="Biotechnology breakthroughs open new possibilities in medicine and treatment development.",
    metadata={
        "Domain": "Technology and Innovation",
        "Topic": "Biotechnology",
        "Category": "Medical Advances",
        "Published Date": "2023-09-25",
        "Source": "Biotech Innovations",
        "Author": "Carl White",
        "Tags": ["Biotechnology", "Medicine"],
        "Keywords": ["biotech", "medical advances"],
        "Language": "English",
        "Sentiment": "Optimistic"
    },
    id=11
)

document_12 = Document(
    page_content="Cloud computing services are transforming business operations, increasing flexibility and scalability.",
    metadata={
        "Domain": "Technology and Innovation",
        "Topic": "Cloud Computing",
        "Category": "Business Technology",
        "Published Date": "2023-10-05",
        "Source": "Business Tech Today",
        "Author": "Amelia Reed",
        "Tags": ["Cloud Computing", "Business"],
        "Keywords": ["cloud services", "scalability"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=12
)

document_13 = Document(
    page_content="Smart city technologies enhance urban living through efficient infrastructure and resource use.",
    metadata={
        "Domain": "Technology and Innovation",
        "Topic": "Smart City",
        "Category": "Urban Development",
        "Published Date": "2023-09-30",
        "Source": "Urban Tech Review",
        "Author": "Sophia Nguyen",
        "Tags": ["Smart City", "Infrastructure"],
        "Keywords": ["smart city", "urban development"],
        "Language": "English",
        "Sentiment": "Positive"
    },
    id=13
)

technology_innovation_docs = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
    document_11,
    document_12,
    document_13
]

