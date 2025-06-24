import zlib

input_file_name='image1.tiff'
output_file_name=input_file_name+".gz"

original_data = open(input_file_name, 'rb').read()
compressed_data = zlib.compress(original_data, zlib.Z_BEST_COMPRESSION)

compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))

print('Compressed: %d%%' % (100.0 * compress_ratio))

f = open(output_file_name, 'wb')
f.write(compressed_data)
f.close()