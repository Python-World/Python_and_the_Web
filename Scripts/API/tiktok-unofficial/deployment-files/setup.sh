mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
[theme]\n\
primaryColor='#F63366'\n\
backgroundColor='#0E1117'\n\
secondaryBackgroundColor='#31333F'\n\
textColor='#FAFAFA'\n\
font='sans serif'\n\
\n\
" > ~/.streamlit/config.toml