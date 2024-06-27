CREATE DATABASE traditional;
use traditional;

CREATE TABLE users
(
    id            INT(11) NOT NULL AUTO_INCREMENT,
    username      VARCHAR(255) DEFAULT NULL,
    password      VARCHAR(255) DEFAULT NULL,
    phone         VARCHAR(11)  DEFAULT NULL,
    personal_info TEXT         DEFAULT NULL,
    photo_url     TEXT         DEFAULT NULL,
    is_banned     CHAR(1)      DEFAULT '0',
    created_at    DATETIME     DEFAULT NULL,
    updated_at    DATETIME     DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

CREATE TABLE admins
(
    id            INT(11) NOT NULL AUTO_INCREMENT,
    username      VARCHAR(255) DEFAULT NULL,
    password      VARCHAR(255) DEFAULT NULL,
    phone         VARCHAR(11)  DEFAULT NULL,
    personal_info TEXT         DEFAULT NULL,
    photo_url     TEXT         DEFAULT NULL,
    created_at    DATETIME     DEFAULT NULL,
    updated_at    DATETIME     DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;


CREATE TABLE works
(
    id          INT NOT NULL AUTO_INCREMENT,
    work_type   VARCHAR(20)  DEFAULT '' COMMENT '作品类型',
    title       VARCHAR(255) DEFAULT '' COMMENT '作品标题',
    worker      VARCHAR(255) DEFAULT '' COMMENT '作者',
    description TEXT         DEFAULT NULL COMMENT '作品简介',
    image_url   TEXT         DEFAULT NULL COMMENT '作品图片',
    content     TEXT         DEFAULT NULL COMMENT '正文文本',
    video_url   TEXT         DEFAULT NULL COMMENT '视频地址',
    created_at  DATETIME     DEFAULT CURRENT_TIMESTAMP COMMENT '数据创建时间',
    updated_at  DATETIME     DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据更新时间',
    PRIMARY KEY (id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4 COMMENT ='作品总表';


CREATE TABLE likes
(
    id         INT NOT NULL AUTO_INCREMENT,
    work_id    INT NOT NULL,
    user_id    INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY work_id (work_id),
    KEY user_id (user_id),
    CONSTRAINT likes_work_id_fk FOREIGN KEY (work_id) REFERENCES works (id) ON DELETE CASCADE,
    CONSTRAINT likes_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4 COMMENT ='点赞表';



CREATE TABLE marks
(
    id         INT NOT NULL AUTO_INCREMENT,
    work_id    INT NOT NULL,
    user_id    INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY work_id (work_id),
    KEY user_id (user_id),
    CONSTRAINT marks_work_id_fk FOREIGN KEY (work_id) REFERENCES works (id) ON DELETE CASCADE,
    CONSTRAINT marks_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4 COMMENT ='收藏表';


CREATE TABLE comments
(
    id         INT  NOT NULL AUTO_INCREMENT,
    work_id    INT  NOT NULL,
    user_id    INT  NOT NULL,
    content    TEXT NOT NULL COMMENT '评论内容',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY work_id (work_id),
    KEY user_id (user_id),
    CONSTRAINT comments_work_id_fk FOREIGN KEY (work_id) REFERENCES works (id) ON DELETE CASCADE,
    CONSTRAINT comments_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4 COMMENT ='评论表';

CREATE TABLE comments_likes
(
    id         INT NOT NULL AUTO_INCREMENT,
    comment_id    INT NOT NULL,
    user_id    INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY comment_id (comment_id),
    KEY user_id (user_id),
    CONSTRAINT comments_likes_comment_id_fk FOREIGN KEY (comment_id) REFERENCES comments (id) ON DELETE CASCADE,
    CONSTRAINT comments_likes_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4 COMMENT ='评论点赞表';

CREATE TABLE comments_marks
(
    id         INT NOT NULL AUTO_INCREMENT,
    comment_id    INT NOT NULL,
    user_id    INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY comment_id_idx (comment_id),
    KEY user_id_idx (user_id),
    CONSTRAINT comments_marks_comment_id_fk FOREIGN KEY (comment_id) REFERENCES comments (id) ON DELETE CASCADE,
    CONSTRAINT comments_marks_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4 COMMENT ='评论收藏表';