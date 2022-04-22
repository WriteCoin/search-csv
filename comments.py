# bookFields = [
#   'bookId',
#   'title',
#   'series',
#   'author',
#   'rating',
#   'description',
#   'language',
#   'isbn',
#   'genres',
#   'characters',
#   'bookFormat',
#   'edition',
#   'pages',
#   'publisher',
#   'publishDate',
#   'firstPublishDate',
#   'awards',
#   'numRatings',
#   'ratingsByStars',
#   'likedPercent',
#   'setting',
#   'coverImg',
#   'bbeScore',
#   'bbeVotes',
#   'price'
# ]

# offsets = []
            # with open(file) as f:
            #   f.readline()
            #   offsets.append(f.tell())
            #   line = f.readline()
            #   while line:
            #     offsets.append(f.tell())
            #     line = f.readline()

            # with open(file) as f:
            #   reader = csv.reader(f)
            #   headers = next(reader)
            #   i = 0
            #   for row in reader:
            #     offset = offsets[i]
            #     value = row[headers.index(key)]
            #     writer.writerow([value, offset])
            #     index[value] = offset
            #     i += 1

            # with open(file) as f:
            #   line = f.readline()
            #   headers = line.replace('"', "").replace('\n', "").split(',')
            #   offset = f.tell()
            #   line = f.readline()
            #   while line:
            #     # values = line.replace('","', ',').replace('\n', "").split('","')
            #     values = line.split('","')
            #     value = values[headers.index(key)]
            #     writer.writerow([value, offset])
            #     index[value] = offset
            #     offset = f.tell()
            #     line = f.readline()

  #                   memory = csv.writer(StringIO)
  #                   memory.writerow(headers)
  #                   memory.writerow(row)

  #                   memory = open(StringIO, 'rb')
  #                   bytes = memory.read()
  #                   memory.close()

  # row_file = open(TEMP_FILE, "wb")
                    # row_file.write(line.encode("utf-8"))
                    # row_file.close()

                    # row_file = open(TEMP_FILE, "rb")
                    # bytes = row_file.read()
                    # row_file.close()