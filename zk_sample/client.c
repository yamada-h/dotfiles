#include <zookeeper/zookeeper.h>
#include <stdio.h>
#include <inttypes.h>
#include <string.h>
#include <unistd.h>

zhandle_t *zh;
clientid_t *client = NULL;

void watcher(zhandle_t *zh, int type, int state, const char *path, void *ctx);

void zk_connect() {
  zh = zookeeper_init("127.0.0.1:2181", watcher, 30000, client, NULL, 0);
  client = zoo_client_id(zh);
}

void watcher(zhandle_t *zh, int type, int state, const char *path, void *ctx) {
  if (type == ZOO_SESSION_EVENT && state == ZOO_EXPIRED_SESSION_STATE) {
    zk_connect();
    return;
  }
  printf("Receive event: %s\n", path);
}

int main() {
  int rc;

  zk_connect();
  printf("clientid=%" PRIx64 ", passwd=%s\n", client->client_id, client->passwd);

  char wpath[256];
  for(int i = 0; i < 100000; i++) {
    snprintf(wpath, 256, "/hoge/fuga/%07d", i);
    rc = zoo_exists(zh, wpath, 1, NULL);
    if (i % 1000 != 0)
      continue;
    printf("watch %s ... ", wpath);
    if (rc == ZOK) {
      printf("Success\n");
    }
    else if (rc == ZNONODE) {
      printf("Success(NONODE)\n");
    }
    else {
      printf("Error: %s\n", zerror(rc));
    }
  }

  /*
  const char *value = "123456789";
  printf("value=%s, size=%ld\n", value, strlen(value));

  for(int i = 0; i < 40000; i++) {
    snprintf(wpath, 256, "/hoge/fuga/%05d", i);
    printf("create %s ... ", wpath);
    rc = zoo_create(zh, wpath, value, strlen(value), &ZOO_OPEN_ACL_UNSAFE, 0, NULL, 0);
    if (rc == ZOK) {
      printf("Success\n");
    }
    else if (rc == ZNODEEXISTS) {
      printf("Exists\n");
    }
    else {
      printf("Error: %d\n", rc);
    }
  }
  */

  zk_connect();

  /*
  printf("Wait for network down\n");
  sleep(60);

  printf("do zoo_exists\n");

  do {
    rc = zoo_exists(zh, "/hoge/fuga/hoo", 1, NULL);
    printf("zoo_exists: %s\n", zerror(rc));
  } while (rc == ZOPERATIONTIMEOUT || rc == ZCONNECTIONLOSS);
  */

  printf("Wait 300 secs and close\n");
  sleep(300);

  zookeeper_close(zh);
}
