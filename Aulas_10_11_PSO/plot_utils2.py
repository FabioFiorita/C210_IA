from matplotlib import pyplot as plt
from PIL import Image
import glob
import os
import shutil

class PlotUtils:

    directory = "pso_plots"
    filename = 'pso_cornfield.gif'

    @staticmethod
    def start_plot():
        if os.path.exists(PlotUtils.directory):
            shutil.rmtree(PlotUtils.directory)
        if not os.path.exists(PlotUtils.directory):
            os.makedirs(PlotUtils.directory)

    @staticmethod
    def plot_particle(particle):
        plt.scatter(particle.position[0], particle.position[1])

    @staticmethod
    def plot_iteration(i):
        plt.title(f"PSO {i}")
        plt.xlim(-20, 20)
        plt.ylim(-20, 20)
        plt.xlabel('x[0]')
        plt.ylabel('x[1]')
        iteration = str(i).zfill(5)
        plt.savefig(f"pso_plots/iteration_{iteration}.png", facecolor = "white", dpi = 75)
        plt.close()

    @staticmethod
    def save():
        images = [Image.open(f) for f in sorted(glob.glob(PlotUtils.directory+"/*"))]
        img = images[0]
        img.save(fp=PlotUtils.filename, format='GIF', append_images=images, save_all=True, duration=200, loop=0)
        if os.path.exists(PlotUtils.directory):
            shutil.rmtree(PlotUtils.directory)
