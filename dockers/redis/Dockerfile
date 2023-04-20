FROM redis:7.0.10
ADD redis/entrypoint.sh /tmp/entrypoint.sh
ADD redis/init.sh /tmp/init.sh
ADD redis/seed.txt /tmp/seed.txt
RUN chmod -R 777 /tmp
ENTRYPOINT ["/tmp/entrypoint.sh"]
CMD ["redis-server"]