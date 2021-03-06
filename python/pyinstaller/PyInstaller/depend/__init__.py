U
    ??_F  ?                   @   s?   d dl Z d dlZd dlZddlmZ ddlmZmZ ddlm	Z
 ddlmZ e
?e?Zedd	? eD ?d
g ?ZG dd? de?ZdS )?    N?   )?get_path_to_egg?   )?TOC?Tree)?log)?ALL_SUFFIXESc                 C   s   g | ]}d | ?qS )?*? )?.0?xr
   r
   ?M/storage/emulated/0/python/pyinstaller/PyInstaller/building/toc_conversion.py?
<listcomp>   s     r   zEGG-INFOc                   @   sL   e Zd ZdZdd? Zdd? Zdd? Zdd	? Zd
d? Ze	dd? ?Z
dd? ZdS )?DependencyProcessorz?
    Class to convert final module dependency graph into TOC data structures.
    TOC data structures are suitable for creating the final executable.
    c                 C   s|   t ? | _t ? | _t ? | _t ? | _|j|jd?D ]H}|j}||krd| j?|?	|?? | j?|?
|?? | j?| ?|?? q.d S )N)?start)?set?	_binaries?_datas?_distributions?-_DependencyProcessor__seen_distribution_paths?flatten?_top_script_node?
identifier?update?binaries?datas?_get_distribution_for_node)?self?graphZadditional_files?node?namer
   r
   r   ?__init__$   s    zDependencyProcessor.__init__c                 C   s~   |j }|sg S t|?}|r$|| jkr(g S | j?|? tt?|??}t|?dksRt?|d }t	?
|j?d|?d?d? |_}|S )znGet the distribution a module belongs to.

        Bug: This currently only handles packages in eggs.
        r   r   T?zip-safe)?zipped?eggr"   )?filenamer   r   ?add?list?pkg_resources?find_distributions?len?AssertionError?zipfile?
is_zipfile?location?has_metadata?_pyinstaller_info)r   r   ?modpath?distpath?dists?dist?infor
   r
   r   r   6   s    
?z.DependencyProcessor._get_distribution_for_nodec                 C   s   dd? | j D ?S )Nc                 S   s   g | ]\}}||d f?qS )?BINARYr
   ?r   r   ?yr
   r
   r   r   f   s     z9DependencyProcessor.make_binaries_toc.<locals>.<listcomp>)r   )r   r
   r
   r   ?make_binaries_tocd   s    z%DependencyProcessor.make_binaries_tocc                 C   s?   t dd? | jD ??}| jD ]`}|jd r|jd s|jd s|?d??? }|j}|rbtj?	||? t
|jtd?}|?|? q|S )Nc                 s   s   | ]\}}||d fV  qdS )?DATANr
   r7   r
   r
   r   ?	<genexpr>i   s     z5DependencyProcessor.make_datas_toc.<locals>.<genexpr>r$   r#   r"   ?top_level.txt??excludes)r   r   r   r0   ?get_metadata?stripr.   ?os?path?joinr   ?PY_IGNORE_EXTENSIONS?extend)r   ?tocr4   ?toplevel?basedir?treer
   r
   r   ?make_datas_toch   s    

??z"DependencyProcessor.make_datas_tocc                 C   sH   g }| j D ]8}|jd r
|jd s
|?dtj?|j? |jdf? q
|S )Nr#   r$   zeggs/?ZIPFILE)r   r0   ?appendrA   rB   ?basenamer.   )r   rF   r4   r
   r
   r   ?make_zipfiles_tocx   s    

? ?z%DependencyProcessor.make_zipfiles_tocc              
   C   s?   ddl m} tj?|d tj?| ??}zt?|? W n8 tk
rl } zdd l}|j|j	kr\? W 5 d }~X Y nX t
?| ??}|?|? W 5 Q R X t|td?S )Nr   )?CONF?workpathr   r=   )?configrO   rA   rB   rC   rM   ?makedirs?OSError?errno?EEXISTr,   ?ZipFile?
extractallr   rD   )ZzipfilenamerO   rP   ?erT   Zzfhr
   r
   r   Z__collect_data_files_from_zip?   s    z1DependencyProcessor.__collect_data_files_from_zipc                 C   s?   t ? }t?d? | jD ]z}|jd r|?d??? }|jd rT| ?|j?}|?	|? q|jd r|j}|rvt
j?||? t|jtd?}|?	|? qq|S )NzLooking for egg data files...r$   r<   r#   r"   r=   )r   ?logger?debugr   r0   r?   r@   ?1_DependencyProcessor__collect_data_files_from_zipr.   rE   rA   rB   rC   r   rD   )r   rF   r4   rG   rI   rH   r
   r
   r   ?make_zipped_data_toc?   s     




z(DependencyProcessor.make_zipped_data_tocN)?__name__?
__module__?__qualname__?__doc__r!   r   r9   rJ   rN   ?staticmethodr[   r\   r
   r
   r
   r   r      s   .
r   )rA   r,   r(   ?depend.utilsr   ?
datastructr   r   ? r   ?logging?compatr   ?	getLoggerr]   rY   r   rD   ?objectr   r
   r
   r
   r   ?<module>   s   
??