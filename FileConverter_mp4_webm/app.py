'''
Inorder for FFMPEG to work do the following
1. conda uninstall -c conda-forge ffmpeg
2. pip install ffmpeg-python

'''

import ffmpeg
import subprocess


class FFMPEG:

    def run_cli_command(self, cmd):
        # Example CLI command: ls -l (list files and directories in long format)
        command = cmd

        # Execute the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Print the output
        print(result.stdout)

    def convert_webm_to_mp4(self, input, output):
        cli_command = ["ffmpeg","-fflags", "+genpts", "-i", input, "-r", "24", output]

        # Execute the command
        result = subprocess.run(cli_command)

        # Print the output
        print(result.stdout)

    def convert_mp4_to_webm(self, input):
        if input.endswith(".mp4"):
            print("mp4 file found: " + input)

            cli_command = ["ffmpeg","-y", "-i", input, input[:-4] + ".webm"]

            result = subprocess.run(cli_command)

            # Print the output
            print(result.stdout)


if __name__ == '__main__':

    # Object Creation
    ffmpeg_obj = FFMPEG()

    # Todo: Subprocess Call
    cmd = "python --version"
    ffmpeg_obj.run_cli_command(cmd)

    # Todo: Webm to MP4
    input_file = 'inputs/webm/test_1.webm'
    output_file = 'output/output.mp4'
    ffmpeg_obj.convert_webm_to_mp4(input_file, output_file)

    # Todo: Mp4 to Webm
    ip_file = "output/output.mp4"
    ffmpeg_obj.convert_mp4_to_webm(ip_file)




