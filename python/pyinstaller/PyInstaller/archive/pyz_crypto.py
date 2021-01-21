U
    ��_u  �                   @   s�   d Z dddddddgZdd	lZdd
lmZmZmZmZmZmZ ed  Z	e_	e�
e	d� dZejeejd� ed�Zdd� Zdd� Zd	S )z 
Logging module for PyInstaller
�	getLogger�INFO�WARN�DEBUG�TRACE�ERROR�FATAL�    N)r   r   r   r   r   r   �   z.%(relativeCreated)d %(levelname)s: %(message)s)�format�level�PyInstallerc              
   C   s(   d}| j d|ddddd�|� d� d S )	N)r   r   r   r   r   ZCRITICALz--log-levelZLEVELr   �loglevelz`Amount of detail in build-time console messages. LEVEL may be one of %s (default: %%(default)s).z, )�choices�metavar�default�dest�help)�add_argument�join)�parserZlevels� r   �9/storage/emulated/0/python/pyinstaller/PyInstaller/log.py�__add_options   s     ��r   c                 C   sH   zt t|j�� �}W n$ tk
r8   | �d|j � Y nX t�|� d S )NzUnknown log level `%s`)�getattr�loggingr   �upper�AttributeError�error�loggerZsetLevel)r   �optsr   r   r   r   �__process_options*   s
    r    )�__doc__�__all__r   r   r   r   r   r   r   r   ZaddLevelNameZFORMATZbasicConfigr   r   r    r   r   r   r   �<module>   s    