import zlib

output_file_name='image1copy1.tiff'
input_file_name=output_file_name+".gz"

compressed_data = open(input_file_name, 'rb').read()
decompressed_data = zlib.decompress(compressed_data)

f = open(output_file_name, 'wb')
f.write(decompressed_data)
f.close()