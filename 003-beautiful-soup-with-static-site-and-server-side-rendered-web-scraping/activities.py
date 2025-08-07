import requests
from bs4 import BeautifulSoup


# Note: the tester relies on this variable, update it if you are running the server on a different port
WEBSITE_BASE_URL = "http://website:3000/"


# Activity 1: Product Titles & Prices
# Return a list of the product titles and prices
#  Ex: ["Sacha the Deer ($3.13)", ...]
def title_and_prices():
    r = requests.get(WEBSITE_BASE_URL)
    #print(r.text) # print out the HTML

    soup = BeautifulSoup(r.text, "html.parser") # parse the HTML

    #product_detail = soup.find("div", {"class": "product-details"}) # you can select by any attribute with this syntax

    #print(product_detail)
    #print(soup)
    totalElements = []
    for element in soup.find_all("div", {"class": "product-details"}):
        paragraphChildren = element.find_all('p')
        h4Children = element.find_all('h4')

        #print(children)
        #print(h4Children[0].text)
        title = h4Children[0].text
        price = paragraphChildren[1].text
        #print(f"title: {title}")
        #print(f"price: {price}")
        totalElements.append(f"{title} ({price})")

    print(totalElements)


    return totalElements

# Activity 2: Get All Colors Available For Each Product
# Return each product's title and color options as a list of strings
#  Ex: ["Sacha the Deer (#000000, #39589e, #9c5145, #dfd3c2)", ...]
def product_colors():
    r = requests.get(WEBSITE_BASE_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = None
    totalColors = []
    totalItems = []

    for product_list in soup.find_all("ul", {"class": "product-list"}):
       product_items = product_list.find_all("li")
#        if not product_items:
#             continue
#        print(product_items)
       for item in product_items:
            #print(item)
            product_details = item.find("div", {"class":"product-details"})
            if not product_details:
                #print("Found empty ")
                continue
                #print(product_details)
            header = product_details.find('h4').text
            #print(header)
            styles = item.find("div", {"class":"styles"})
            #colors = styles.find("div", {"class":"style-picker"})
            if not styles:
                continue
            #print(styles)
            colors = styles.find("div", {"class":"style-picker"})
            color_divs = colors.find_all("div", {"data-item-id": True})
            #print(colors)
            #print("--------------")
            for div in color_divs:
                #print(div)
                style_attr = div.get('style', '')
                #print(style_attr)
                if 'background-color' in style_attr:
                    color = style_attr.split(':')[1].strip()

                    #print(color)
                    totalColors.append(color)
            #print("--------------")
            #print(header)
            #print(totalColors)
            commaSeparatedString = ', '.join(totalColors)
            totalItems.append(f"{header} ({commaSeparatedString})")
            totalColors = []
            commaSeparatedString = ''
    print(totalItems)
    return totalItems

# Activity 3: Get All Product's Material
# Return each product's title and material as a list of strings
#  Ex: ["Bumble the Elephant made of 70% Cotton, 30% Nylon", ...]
def product_materials():
    r = requests.get(WEBSITE_BASE_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    endpoints = []
    fullDetails = []
    for unorderedListItem in soup.find_all('ul', {"class": "product-list"}):
        #print(item)
#          listItems = item.find_all('li')
         #print(unorderedListItem)
         for listItem in unorderedListItem.find_all("li"):
            styles = listItem.find("div", {"class": "styles"})
            if not styles:
                continue
            style = styles.find("div", {"class": "style"})
            #print(style)
            if not style:
                continue
            aTag = style.find("a", href=True)
            #print(aTag['href'])
            if not aTag:
                continue
            endpoints.append(aTag['href'])



         print(endpoints)
         for endpoint in endpoints:
            #print("http://website:3000" + endpoint)
            response = requests.get("http://website:3000" + endpoint)
            #print(html)
            html = BeautifulSoup(response.text, 'html.parser')
            for div in html.find_all("div", {"class": "product-details"}):
#                 print(div)
                header = div.find("h3")
                material = div.find("p", {"id": "material"})
                print(f"header: {header.text}, material: {material.text}")
                fullDetails.append(f"{header.text} made of {material.text}")



    print(fullDetails)


    return fullDetails

# Activity 4: Filter all the products from highest reviewed to lowest reviewed
# Return a list of the product titles and average rating as a touple
#   Ex: [('Scar the Lion', 5), ...]
def highest_reviewed():
    r = requests.get(WEBSITE_BASE_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    endpoints = []
    fullDetails = []
    for unorderedListItem in soup.find_all('ul', {"class": "product-list"}):
            #print(item)
    #          listItems = item.find_all('li')
             #print(unorderedListItem)
         for listItem in unorderedListItem.find_all("li"):
            styles = listItem.find("div", {"class": "styles"})
            if not styles:
                continue
            style = styles.find("div", {"class": "style"})
            #print(style)
            if not style:
                continue
            aTag = style.find("a", href=True)
            #print(aTag['href'])
            if not aTag:
                continue
            endpoints.append(aTag['href'])

            #print(endpoints)
    for endpoint in endpoints:
        #print("http://website:3000" + endpoint)
        response = requests.get("http://website:3000" + endpoint)
        #print(html)
        html = BeautifulSoup(response.text, 'html.parser')
        for div in html.find_all("div", {"class": "product-details"}):
#                 print(div)
            header = div.find("h3")
            print(header)
            #starsList = div.find_all("div", {"class": "product-rating"})
            productRating = div.find("div", {"class" : "product-rating"})
            #print(productRating)
            checked = productRating.find_all("span", {"class": "checked"})
            print(len(checked))
            fullDetails.append((header.text,len(checked)))
                    #print(len(checked))
#                     rating = productRating.find("div", {"class": "star-rating"})
                    #print(len(rating.find_all("span", {"class": "checked"})))
                    #print(len(span))

#                     for star in starsList:
#                         rating = star.find_all("span", {"class": "fa fa-star checked"})
#                         #print(len(rating))
# #                     stars = starsList.find_all("span", {"class": "fa fa-star checked"})
# #                     print(starsList)
#                         fullDetails.append((header.text, len(rating)))


    sortedDetails = sorted(fullDetails, key=lambda x: x[1], reverse=True)

    print(sortedDetails)
    return sortedDetails

# Activity 5: Product Availability
# Not all products are available, look at `Gerald the Giraffe`
# Return a list of strings of all products and their availability
#  Ex: ["Sacha the Deer is available: True", ...]
def product_availability():
    r = requests.get(WEBSITE_BASE_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    endpoints = []
    fullDetails = []
    for unorderedListItem in soup.find_all('ul', {"class": "product-list"}):
                #print(item)
        #          listItems = item.find_all('li')
                 #print(unorderedListItem)
         for listItem in unorderedListItem.find_all("li"):
            styles = listItem.find("div", {"class": "styles"})
            if not styles:
                continue
            style = styles.find("div", {"class": "style"})
            #print(style)
            if not style:
                continue
            aTag = style.find("a", href=True)
            #print(aTag['href'])
            if not aTag:
                continue
            endpoints.append(aTag['href'])

                #print(endpoints)
    for endpoint in endpoints:
        #print("http://website:3000" + endpoint)
        response = requests.get("http://website:3000" + endpoint)
        #print(html)
        html = BeautifulSoup(response.text, 'html.parser')
        for div in html.find_all("div", {"class": "product-details"}):
#                 print(div)
            header = div.find("h3")
            #print(header)
            checkoutButton = div.find("div", {"class": "button"})
            #print(checkoutButton.text)
            if checkoutButton and "Add to cart" in checkoutButton.text:
                print(f"Header: {header.text} {checkoutButton.text}")
                fullDetails.append(f"{header.text} is available: True")
            else:
                fullDetails.append(f"{header.text} is available: False")
                #starsList = div.find_all("div", {"class": "product-rating"})
    print(fullDetails)
    return fullDetails

# Activity 6: Scrape Reviews For Each Product
# Return a dictionary with structure {"product_title": [{"rating": "5", "review_title": "Great!", "review_full": "I love it"}, ...], ...}
# Ex: {"Sacha the Deer": [{'rating': '5', 'review_title': 'V neck', 'review_full': 'Great shirt. love the detail in back. feminine and different than the average t'}, ...]}
def product_reviews():
     r = requests.get(WEBSITE_BASE_URL)
     soup = BeautifulSoup(r.text, 'html.parser')
     endpoints = []
     fullDetails = {}

     for unorderedListItem in soup.find_all('ul', {"class": "product-list"}):
        for listItem in unorderedListItem.find_all("li"):
            styles = listItem.find("div", {"class": "styles"})
            if not styles:
                continue
            style = styles.find("div", {"class": "style"})
            #print(style)
            if not style:
                continue
            aTag = style.find("a", href=True)
            #print(aTag['href'])
            if not aTag:
                continue
            endpoints.append(aTag['href'])
     for endpoint in endpoints:
        response = requests.get("http://website:3000" + endpoint)
        #print(html)
        html = BeautifulSoup(response.text, 'html.parser')
        details = html.find("div", {"class": "product-details"})
        header = details.find("h3").text
        print(details.find("h3").text)
        ratingInfo = []

        reviews = html.find("div", {"class": "product-reviews"})
        productRatings = reviews.find("div", {"class": "product-ratings"})
        ratingDetails = productRatings.find_all("div", {"class": "product-rating"})
        for rating in ratingDetails:
            #print(rating.find("div", {"class": "rating-title"}).text)
            ratingTitle = rating.find("div", {"class": "rating-title"}).text
            starRating = rating.find("div", {"class": "star-rating"})
            ratingNumber = starRating.find("span", {"class": "rating-number"}).text
            #print(ratingNumber)
            ratingReview = rating.find("div", {"class": "rating-review"}).text
            #print(ratingReview)
            ratingInfo.append({
            "rating": ratingNumber,
            "review_title": ratingTitle,
            "review_full": ratingReview
            })
            fullDetails[header] = ratingInfo


     print(fullDetails)



     return fullDetails

if __name__ == "__main__":
    # Optional: You can call your methods here if you want to test them without running the tester
    # print(title_and_prices())
    #title_and_prices()
    #product_colors()
    #product_materials()
    #highest_reviewed()
    #product_availability()
    product_reviews()
    pass