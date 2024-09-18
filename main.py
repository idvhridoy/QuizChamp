from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)
# List of participants
contestants = [
    {"name": "Nadira Zaman Doly", "image": "https://scontent.fdac24-1.fna.fbcdn.net/v/t39.30808-1/444935963_1622303851936803_1381208811658265675_n.jpg?stp=dst-jpg_s200x200&_nc_cat=110&ccb=1-7&_nc_sid=0ecb9b&_nc_eui2=AeHnaHICD5saZ5gYINxjIWftXnwNxVAUgHxefA3FUBSAfDeM2LzQTi6x_kfgresx2ZciBlmkNtVt5wolcVspG0Sf&_nc_ohc=vD4gfHC_AW0Q7kNvgEAm0i2&_nc_ht=scontent.fdac24-1.fna&_nc_gid=AtXEsj6mfwbuWmfePbxlc4-&oh=00_AYAzXW87ZhPZ_eqhnE7YRZXjlkYu31hBsZsXAExHW0v5ow&oe=66EF2F94"},
    {"name": "Ramesha Noor", "image": "https://scontent.fdac24-4.fna.fbcdn.net/v/t39.30808-1/440229354_331954436569848_3280304261967179329_n.jpg?stp=c0.0.600.600a_dst-jpg_s200x200&_nc_cat=109&ccb=1-7&_nc_sid=0ecb9b&_nc_eui2=AeGSeaRvgDlyjKyeRPX8Xu-07ND8Y1Rbmy_s0PxjVFubLydMcu7Z9QXyNQmOeOU62ySCHG411A5kGHG6rSWQ5vrd&_nc_ohc=zAfBxWbj1gkQ7kNvgHQe94-&_nc_ht=scontent.fdac24-4.fna&_nc_gid=AOfqF7V2HYhkIl63bLEIgFF&oh=00_AYCMQsx5NB_aJlSNHlqHdBrq8AyZhDUJnh-jLDZ46QC8MA&oe=66EEFDE3"},
    {"name": "Kobita Afrose", "image": "https://scontent.fdac24-4.fna.fbcdn.net/v/t39.30808-1/436223871_1161809721643167_6850096620703971971_n.jpg?stp=dst-jpg_s200x200&_nc_cat=109&ccb=1-7&_nc_sid=0ecb9b&_nc_eui2=AeE-HU5_6I3uSi5M9NRR-DenHgypvlOjBP8eDKm-U6ME_5wgGxannKQ-37Ngke4bLm9Pc93BVOhAikCcnaGil4M6&_nc_ohc=jolHnzz0tBAQ7kNvgHy3392&_nc_ht=scontent.fdac24-4.fna&_nc_gid=AeQGsscl0nLY9Mp9Y1h-8qh&oh=00_AYC-PDWNM27_NAwHLlo3IHXLgjtn87dLVk2wCCoomm2hGA&oe=66EEFFF0"},
    {"name": "Fatima Jannat Sadia", "image": "https://scontent.fdac24-2.fna.fbcdn.net/v/t39.30808-1/459589513_932135642276600_8221654217470902421_n.jpg?stp=c0.18.540.540a_cp0_dst-jpg_s40x40&_nc_cat=108&ccb=1-7&_nc_sid=0ecb9b&_nc_eui2=AeGZLt4vWPti_2W4di1EiBfkVijWyGUoArBWKNbIZSgCsO8mEjoVlNsc-Fh5W8ctH8hBekbajjWYzuWQnALOFFC_&_nc_ohc=W4nSfQBW3BsQ7kNvgHXL5st&_nc_ht=scontent.fdac24-2.fna&_nc_gid=ApIUzgWgA-SDS3DUHTJVskI&oh=00_AYCJ2pISkhPJZu0z5fm-Uy0RZgW2xXlpTieV6f_IBJuoYw&oe=66EF2801"},
    {"name": "Farzana Easmin", "image": "https://scontent.fdac24-4.fna.fbcdn.net/v/t39.30808-1/380770689_240644652282258_1594931542392765199_n.jpg?stp=dst-jpg_s200x200&_nc_cat=107&ccb=1-7&_nc_sid=0ecb9b&_nc_eui2=AeEfKTMxTmIWfYx9ZxcgxZxJoPtPXuaetxmg-09e5p63GegofyX4hi7Zp3eABC3zDFUf48CzSFbdFEPHgnWA1ORy&_nc_ohc=8pgGXexgQzsQ7kNvgGbIG3S&_nc_ht=scontent.fdac24-4.fna&_nc_gid=AeUcmohKxNpd0uwpxCXL1F_&oh=00_AYCb9Hzo6YHog6D4ZOWai5HD0rB28q5bNKcuz83tKAkxHw&oe=66EF1C53"},
    {"name": "Shahina Begum", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsok3LrTKWF6w69YcC0vvsbtQGBYO7bMbKAA&s"},
    {"name": "Suhana Rahman", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSznYoOn2HvZWxiufAyckBdrNVgP3uUrwwcnw&s"},
    {"name": "Parvin Sultana", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXTEVTGp-7L7jvgykOO3Eng2_AT9tC36KSAw&s"},
    {"name": "Nazma Khatun", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4nM5Fonn3BoB2crHRcPPD13NjXjuY2JKPwQ&s"},
    {"name": "Shamima Akter", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjBbDmk6bP5OM-ACt2uL2laMYlAeLwFRqfqw&s"},
    {"name": "Taslima Jahan", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRl6Zc1Kc1MojQsHR6fTnczTJ5uxYulkcoIjQ&s"},
    {"name": "Laila Nargis", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcxQ32AdfMJt28qStJxIiuJ5cM9TKwuvmcDQ&s"},
    {"name": "Mithila Akhter", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHyK6FOzdTmsLcYbX-kDJvA0QPqBbjsOZIyA&s"},
    {"name": "Sadia Islam Nisha", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6C3dQo4ZbZtK3FQr6aA5or8Rwst6myOcCrw&s"},
    {"name": "Sumaiya Akhter", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUMyyb9J52PjiWNhS34iF7MSgNDlaXQ9rhvA&s"},
]

@app.route('/')
def index():
    return render_template('index.html', contestants=contestants)


@app.route('/draw', methods=['GET'])
def draw():
    # This route is called when the "Choose Winner" button is clicked
    # Redirect to the winner page
    return redirect(url_for('winner'))

@app.route('/winner')
def winner():
    # Pass contestants to the winner.html page
    return render_template('winner.html', contestants=contestants)

if __name__ == '__main__':
    app.run(debug=True)