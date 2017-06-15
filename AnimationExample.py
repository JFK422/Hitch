def slideInWidget(self, widget):
        if self.indexOf(widget) == -1 or widget is self.currentWidget():
            return

        if self._active:
            return

        self._active = True

        prev_widget = self.currentWidget()
        next_widget = widget

        if direction == self.Automatic:
            if self.indexOf(prev_widget) < self.indexOf(next_widget):
                direction = self.BottomToTop if self.verticalMode else self.RightToLeft
            else:
                direction = self.TopToBottom if self.verticalMode else self.LeftToRight

        width = self.frameRect().width()
        height = self.frameRect().height()

        # the following is important, to ensure that the new widget has correct geometry information when sliding in the first time
        next_widget.setGeometry(0, 0, width, height)

        if direction in (self.TopToBottom, self.BottomToTop):
            offset = QPoint(0, height if direction==self.TopToBottom else -height)
        elif direction in (self.LeftToRight, self.RightToLeft):
            offset = QPoint(width if direction==self.LeftToRight else -width, 0)

        # re-position the next widget outside of the display area
        prev_widget_position = prev_widget.pos()
        next_widget_position = next_widget.pos()

        next_widget.move(next_widget_position - offset)
        next_widget.show()
        next_widget.raise_()

        prev_widget_animation = QPropertyAnimation(prev_widget, "pos")
        prev_widget_animation.setDuration(self.animationDuration)
        prev_widget_animation.setEasingCurve(QEasingCurve(self.animationEasingCurve))
        prev_widget_animation.setStartValue(prev_widget_position)
        prev_widget_animation.setEndValue(prev_widget_position + offset)

        next_widget_animation = QPropertyAnimation(next_widget, "pos")
        next_widget_animation.setDuration(self.animationDuration)
        next_widget_animation.setEasingCurve(QEasingCurve(self.animationEasingCurve))
        next_widget_animation.setStartValue(next_widget_position - offset)
        next_widget_animation.setEndValue(next_widget_position)

        self._animation_group.clear()
        self._animation_group.addAnimation(prev_widget_animation)
        self._animation_group.addAnimation(next_widget_animation)
        self._animation_group.start()