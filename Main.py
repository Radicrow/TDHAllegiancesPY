import pandas as pd
import plotly.express as px


data = {
    "ThunderClan": {
        "Leader": [("Firestar", "male")],
        "Deputy": [("Brambleclaw", "male")],
        "Medicine Cat": [("Jayfeather", "male")],
        "Warriors": [
            ("Graystripe", "male"),
            ("Dustpelt", "male"),
            ("Sandstorm", "female"),
            ("Brackenfur", "male"),
            ("Cloudtail", "male"),
            ("Brightheart", "female"),
            ("Millie", "female"),
            ("Thornclaw", "male"),
            ("Squirrelflight", "female"),
            ("Leafpool", "female"),
            ("Spiderleg", "male"),
            ("Birchfall", "male"),
            ("Whitewing", "female"),
            ("Berrynose", "male"),
            ("Hazeltail", "female"),
            ("Mousewhisker", "male"),
            ("Cinderheart", "female"),
            ("Lionblaze", "male"),
            ("Foxleap", "male"),
            ("Icecloud", "female"),
            ("Toadstep", "male"),
            ("Rosepetal", "female"),
            ("Briarlight", "female"),
            ("Blossomfall", "female"),
            ("Bumblestripe", "male"),
            ("Dovewing", "female"),
            ("Ivypool", "female"),
            ("Hollyleaf", "female")
        ],
        "Queens": [
            ("Sorreltail", "female"),
            ("Ferncloud", "female"),
            ("Daisy", "female"),
            ("Poppyfrost", "female")
        ],
        "Elders": [
            ("Mousefur", "female"),
            ("Purdy", "male")
        ]
    },
    "ShadowClan": {
        "Leader": [("Blackstar", "male")],
        "Deputy": [("Rowanclaw", "male")],
        "Medicine Cat": [("Littlecloud", "male"),],
        "Warriors": [
            ("Oakfur", "male"),
            ("Smokefoot", "male"),
            ("Toadfoot", "male"),
            ("Applefur", "female"),
            ("Crowfrost", "male"),
            ("Ratscar", "male"),
            ("Snowbird", "female"),
            ("Tawnypelt", "female"),
            ("Olivenose", "female"),
            ("Owlclaw", "male"),
            ("Shrewfoot", "female"),
            ("Scorchfur", "male"),
            ("Redwillow", "male"),
            ("Tigerheart", "male"),
            ("Dawnpelt", "female"),
            ("Pinenose", "female"),
            ("Ferretclaw", "male"),
            ("Starlingwing", "male")
        ],
        "Queens": [
            ("Kinkfur", "female"),
            ("Ivytail", "female")
        ],
        "Elders": [
            ("Cedarheart", "male"),
            ("Tallpoppy", "female"),
            ("Snaketail", "male"),
            ("Whitewater", "female")
        ]
    },
    "WindClan": {
        "Leader": [("Onestar", "male")],
        "Deputy": [("Ashfoot", "female")],
        "Medicine Cat": [("Kestrelflight", "male")],
        "Warriors": [
            ("Crowfeather", "male"),
            ("Owlwhisker", "male"),
            ("Whitetail", "female"),
            ("Nightcloud", "female"),
            ("Gorsetail", "male"),
            ("Weaselfur", "male"),
            ("Harespring", "male"),
            ("Leaftail", "male"),
            ("Antpelt", "male"),
            ("Emberfoot", "male"),
            ("Heathertail", "female"),
            ("Breezepelt", "male"),
            ("Sedgewhisker", "female"),
            ("Swallowtail", "female"),
            ("Sunstrike", "female")
        ],
        "Apprentices":  [
            ('Whiskerpaw', 'male'),
            ('Furzepaw ', 'female'),
            ('Boulderpaw ', 'male'),
        ],
        "Elders": [
            ("Webfoot", "male"),
            ("Tornear", "male")
        ]
    },
    "RiverClan": {
        "Leader": [("Mistystar", "female")],
        "Deputy": [("Reedwhisker", "male")],
        "Medicine Cat": [("Mothwing", "female"),
                            ("Willowshine", 'Female')],
        "Warriors": [
            ("Graymist", "female"),
            ("Mintfur", "male"),
            ("Icewing", "female"),
            ("Minnowtail", "female"),
            ("Pebblefoot", "male"),
            ("Mallownose", "male"),
            ("Robinwing", "male"),
            ("Beetlewhisker", "male"),
            ("Petalfur", "female"),
            ("Grasspelt", "male")
        ],
        "Apprentices":  [
            ('Hollowpaw', 'male'),
            ('Troutpaw', 'female'),
            ('Mossypaw', 'female'),
            ('Rushpaw', 'male'),
        ],
        "Queens": [
            ("Duskfur", "female"),
            ("Mosspelt", "female")
        ],
        "Elders": [
            ("Dapplenose", "female"),
            ("Pouncetail", "male")
        ]
    }
}

def create_clan_df(clan_name, clan_data):
    records = []
    for role, members in clan_data.items():
        for member in members:
            name, gender = member[:2]

            records.append({
                'Clan': clan_name,
                'Role': role,
                'Name': name,
                'Gender': gender,

            })
    return pd.DataFrame(records)


dfs = [create_clan_df(clan, details) for clan, details in data.items()]
df_all_clans = pd.concat(dfs, ignore_index=True)

gender_counts = df_all_clans.groupby(['Clan', 'Gender']).size().unstack(fill_value=0)
gender_ratios = gender_counts.div(gender_counts.sum(axis=1), axis=0) * 100


fig = px.bar(df_all_clans, x='Clan', color='Role', text='Name',
             title='Clan Sizes and Allegiances in THE LAST HOPE',
             labels={'Clan': 'Clan', 'count': 'Number of Members'},
             category_orders={'Role': ['Leader', 'Deputy', 'Medicine Cats', 'Warriors', 'Apprentices', 'Queens', 'Elders']})

for clan in df_all_clans['Clan'].unique():
    ratios = gender_ratios.loc[clan]
    male_ratio = ratios.get('male', 0)
    female_ratio = ratios.get('female', 0)
    fig.add_annotation(
        x=clan,
        y=0,
        text=f"Male: {male_ratio:.1f}%\n\nFemale: {female_ratio:.1f}%",
        showarrow=False,
        align="center",
        font=dict(size=12, color="Black"),
        xanchor='center',
        yanchor='top'
    )


fig.update_layout(barmode='stack')
fig.show()

df_all_clans.to_csv(("df_all_clans.csv"))