def room():
  st.plotly_chart(px.pie(df[df['CountryLive'] == 'United States of America'], names="JobInterest"))
