import os
import shutil

src_dir = r'F:\github_projects\book\champion-yang.github.io\projects\site'
dst_dir = r'F:\github_projects\book\champion-yang.github.io'


if __name__ == "__main__":

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    for file in os.listdir(src_dir):
        src_file = os.path.join(src_dir, file)
        dst_file = os.path.join(dst_dir, file)
        if os.path.isfile(src_file):
            shutil.copy(src_file, dst_file)