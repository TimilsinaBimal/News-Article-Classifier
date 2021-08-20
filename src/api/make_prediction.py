from predict import predict

data = input("Enter article: ")

# data = "The 2018 FIFA World Cup starts June 14 in Russia, and now it has an official song.  Producer Diplo and reggaeton star Nicky Jam collaborate on “Live It Up,” which also features Albanian singer Era Istrefi and actor Will Smith, who is trying to restart his music career. Traditionally, over the last two decades, each World Cup has had an official song. The song for the 2010 World Cup in South Africa was “Waka Waka” by Shakira. For the 2014 World Cup in Brazil, the song was “We Are One (Ole Ola)” by Pitbull.  "
prediction = predict(data)
print(f"CATEGORY: {prediction}")
