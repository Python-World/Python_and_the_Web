import streamlit as st
import pandas as pd
from TkApi import TkTkUser


#chromewebdriver version chrome=95.0.4638.54

st.title('Enter the tiktok user')
input = st.text_input('Example: therock', value='therock')
veri_fp_input = st.text_input('Enter custom verifyFp', 'verify_kv2emkaa_mYpSNrSe_ZzZZ_4y7V_9Pja_9IfMJCKxofNp')
st.markdown('[How to get Custom verifyFp](https://youtu.be/zwLmLfVI-VQ)')


try:
    if input != '':
        st.write('fetching tiktok user data for the {}...'.format(input))
        user = TkTkUser(str(input), custom_verifyFp=veri_fp_input)

        df = pd.DataFrame({"Feature": ['username', 'Description', 'nickname', 'followerCount', 'followingCount',
                                       'videoCount', 'is_private', 'is_verified'],
                           "Value": [user.username, user.description, user.nickname, user.followerCount,
                                     user.followingCount, user.videoCount, user.is_private, user.is_verified]})

        st.write(df.astype(str))

        st.info('Created on: 21th October 2021 by [Aditya Rajgor](https://github.com/Aditya-Rajgor)')



    else:
        st.write('input the verifyFp string')
        pass

except Exception as e:
    print(e)
    #st.write(e)

st.write('If you are in India, You might have to use VPN profile')

